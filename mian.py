import turtle
import math

def move_to_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(x1, y1, x2, y2, color):
    turtle.pencolor(color)
    move_to_point(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def draw_group_separator():
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    turtle.speed(0)  
    turtle.setup(width=450, height=450)  

    file_name = input("Enter the name of the input file: ")

    total_distance = 0

    try:
        with open(file_name, 'r') as file:
            current_color = "black"
            prev_point = None
            for line in file:
                line = line.strip()
                if line == "stop":
                    turtle.penup()
                    prev_point = None
                    continue

                command, *args = line.split()
                if command == 'line':
                    x1, y1, x2, y2 = map(float, args)
                    draw_line(x1, y1, x2, y2, current_color)
                    if prev_point is not None:
                        total_distance += calculate_distance(x1, y1, prev_point[0], prev_point[1])
                    prev_point = (x2, y2)
                elif command == 'color':
                    current_color = args[0]
                elif command == 'move':
                    x, y = map(float, args)
                    move_to_point(x, y)
                    prev_point = (x, y)
                else:
                    print(f"Unknown command: {command}")

    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file.close()

    turtle.penup()
    turtle.goto(200, -200)
    turtle.pendown()
    turtle.write(f"Total Distance: {total_distance:.2f}", align="center", font=("Arial", 16, "normal"))

    input("Press Enter to close the window.")
    turtle.bye()

if __name__ == "__main__":
    main()


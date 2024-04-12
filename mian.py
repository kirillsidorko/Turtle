import turtle
import math

def move_to_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(x1, y1, x2, y2, color):
    turtle.pencolor(color)
    move_to_point(x1, y1)
    turtle.goto(x2, y2)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    turtle.speed(0)
    turtle.setup(width=450, height=450)

    file_name = input("Enter the name of the input file: ")
    total_distance = 0
    prev_point = None
    first_point = True
    current_color = "black"

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line == "stop":
                    turtle.penup()
                    prev_point = None
                    first_point = True
                    continue

                parts = line.split()
                if len(parts) < 3:  
                    print(f"Skipping malformed line: {line}")
                    continue

                color, x, y = parts[0], int(parts[1]), int(parts[2])

                if first_point:
                    move_to_point(x, y)
                    first_point = False
                else:
                    if prev_point is not None:
                        total_distance += calculate_distance(prev_point[0], prev_point[1], x, y)
                    draw_line(prev_point[0], prev_point[1], x, y, color)

                prev_point = (x, y)
                current_color = color

    except FileNotFoundError:
        print(f"File not found: {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

    turtle.penup()
    turtle.goto(200, -200)
    turtle.pendown()
    turtle.write(f"Total Distance: {total_distance:.2f}", align="center", font=("Arial", 16, "normal"))

    input("Press Enter to close the window.")
    turtle.bye()

if __name__ == "__main__":
    main()


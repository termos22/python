import turtle

radius = 100
angular_speed = 2

window = turtle.Screen()
window.tracer(0)
window.bgcolor(50 / 255, 50 / 255, 50 / 255)

main_dot = turtle.Turtle()
main_dot.pensize(5)
main_dot.shape("circle")
main_dot.color(0, 160 / 255, 193 / 255)
main_dot.penup()
main_dot.setposition(0, -radius)
main_dot.pendown()

vertical_dot = turtle.Turtle()
vertical_dot.shape("circle")
vertical_dot.color(248 / 255, 237 / 255, 49 / 255)
vertical_dot.penup()
vertical_dot.setposition(main_dot.xcor() + 2 * radius, main_dot.ycor())

vertical_plot = vertical_dot.clone()
vertical_plot.hideturtle()
start_x = int(vertical_plot.xcor())
# Get range of x-values from position of dot to edge of screen
x_range = range(start_x, window.window_width() // 2 + 1)
# Create a list to store the y-values to draw at each
# point in x_range.
vertical_values = [None for _ in x_range]
# You can populate the first item in this list
# with the dot's starting height
vertical_values[0] = vertical_plot.ycor()

horizontal_dot = turtle.Turtle()
horizontal_dot.shape("circle")
horizontal_dot.color(242 / 255, 114 / 255, 124 / 255)
horizontal_dot.penup()
horizontal_dot.setposition(main_dot.xcor(), main_dot.ycor() - radius)


while True:
    main_dot.circle(radius, angular_speed)

    vertical_dot.sety(main_dot.ycor())

    horizontal_dot.setx(main_dot.xcor())

    window.update()

turtle.done()

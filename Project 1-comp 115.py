import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.hideturtle()

# Colors for the mandala
colors = [ "red", "orange", "yellow",
    "lime", "cyan", "blue",
    "purple", "magenta"]

# Draw the big mandala pattern
for i in range(36):
    t.color(colors[i % len(colors)])

    for j in range(6):
        t.circle(80)
        t.left(60)

    t.left(10)

# Draw the small mandela
for i in range(12):
    t.color(colors[i % len(colors)])
    t.circle(40)
    t.left(30)

turtle.done()


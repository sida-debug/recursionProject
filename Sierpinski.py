import math
import turtle
turt = turtle.Turtle()
def sierpinski(x, y, t):
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    topx = x/2
    topy = math.sqrt(pow(x, 2)-pow(topx, 2))*t
    turt.goto(topx, topy)
    turt.goto(0, 0)
    turt.goto(x, y)
    t*-1
    midbot = [x/2, y/2]
    midright = []
    sierpinski(500, 0, t)

    turtle.mainloop()

#sierpinski(500, 0, 1)

hi = [500, 0]
turt.goto(hi)

import turtle
def draw_sierpinski(length,depth):
    t = turtle.Turtle()
    if depth==0:
        for i in range(0,3):
            t.forward(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.forward(length/2)
        draw_sierpinski(length/2,depth-1)
        t.back(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.back(length/2)
        t.right(60)
    turtle.mainloop()
draw_sierpinski(5000,10)
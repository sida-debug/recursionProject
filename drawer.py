import turtle
def drawer(filename):
    turt = turtle.Turtle()
    f = open(filename, "r")
    lineDict = {}
    for i in f:
        lineDict[len(lineDict)+1] = int(i.split())
    for i in range(len(lineDict)):
        if lineDict(i) == "UP":
            turt.hideturtle()
        elif lineDict(i) == "DOWN":
            turt.showturtle()
        else:
            turt.goto(lineDict(i)[0], lineDict(i)[0])

drawer("C:\Users\sid\Downloads\draw.txt")
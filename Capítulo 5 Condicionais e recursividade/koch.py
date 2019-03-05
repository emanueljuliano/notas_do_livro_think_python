import turtle
bob = turtle.Turtle()
def koch(t, lengh):
    if lengh < 30:
        t.fd(lengh)
        return
    m = lengh / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

def snow_flake(t, lengh):
    for i in range (3):
        koch(t, lengh)
        t.rt(120)

snow_flake(bob, 100)

turtle.mainloop()
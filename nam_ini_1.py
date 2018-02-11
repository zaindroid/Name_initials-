
import turtle

t1= turtle.Turtle()
t1.hideturtle()
t1.pensize(30)
t1.pencolor("white")

t1.screen.bgcolor("#3498DB")
                  
                  
                    
def draw_z(x,y,o):    
    o.penup()
    o.goto(x,y)
    o.pendown()
    o.speed(2)
    o.fd(100)
    o.rt(135)
    o.fd(140)
    o.lt(135)
    o.fd(100)

def draw_u(x,y,o):    
    o.penup()
    o.goto(x,y)
    o.pendown()
    o.speed(2)
    o.rt(90)
    o.fd(100)
    o.rt(90)
    o.fd(80)
    o.rt(90)
    o.fd(100)
 
def draw_h(x,y,o):    
    o.penup()
    o.goto(x,y)
    o.pendown()
    o.speed(2)    
    o.fd(100)
    o.bk(50)
    o.rt(90)
    o.fd(70)
    o.rt(90)
    o.fd(50)
    o.bk(100)
    
draw_z(-180,0,t1)
t1.screen.bgcolor("#FFC300")
draw_u(90,0,t1)
t1.screen.bgcolor("#88f40c")
draw_h(170,-100,t1)    

t1.exitonclick()
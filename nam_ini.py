
import turtle

t1= turtle.Turtle()
t2= turtle.Turtle()
t3= turtle.Turtle()

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

t1.pensize(30)
t2.pensize(30)
t3.pensize(30)

t1.pencolor("white")
t2.pencolor("white")
t3.pencolor("white")

t1.screen.bgcolor("#3498DB")
                             
# Setting up instances  
## instance 1               
t1.penup()
t1.goto(-180,0)
t1.pendown()
t1.speed(3)
## instance 2
t2.penup()
t2.goto(90,0)
t2.pendown()
t2.speed(3)
## instance 3
t3.penup()
t3.goto(170,-100)
t3.pendown()
t3.speed(5) 

#main drawing

t1.fd(100)
t1.rt(135)
t2.rt(90)
t2.fd(100)
t3.lt(90)
t3.fd(100)
t3.bk(50)
t1.screen.bgcolor("#88f40c")
                  
t1.fd(140)
t2.rt(90)
t2.fd(80)
t3.rt(90)
t3.fd(70)


                  
t1.lt(135)
t1.fd(100)
t2.rt(90)
t2.fd(100)
t3.rt(90)
t3.fd(50)
t3.bk(100)
t1.screen.bgcolor("#ffda49")    
t1.exitonclick()
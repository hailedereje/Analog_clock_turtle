#Data structur and allgorithm assignment
#made by "Haile Dereje"#
import turtle
import time
#scrn stands for the screen i am worming on and tur stands for the turtle which draws the entier clock 
scrn=turtle.Screen()

tur=turtle.Turtle()
scrn.tracer(0)


def analog_clock(h,m,s):
    
    #draw the outer circle for the clock
    tur.speed(0)
    n=1
    tur.width(6)
    tur.speed(0)
    tur.up()

    tur.setpos(0,230)
    tur.setheading(180)
    tur.pd()
    tur.color('black')
    tur.circle(230)
    tur.up()
    tur.width(6)
    tur.setpos(0,10)
    tur.color('blue')
    tur.pd()
    tur.circle(10)
    tur.up()
    tur.setpos(0,0)
    tur.setheading(60)
    tur.width(8)
    tur.color('black')
    
    #for the second and hour indicator segments
    for i in range(12):
        tur.up()
        tur.fd(200)
        tur.pd()
        tur.fd(30)
        tur.up()
        tur.bk(60)
        tur.pd()
    
        tur.up()
        tur.setpos(0,0)
        tur.color('black')
        tur.rt(5)
        for i in range(5) :
                tur.up()
                tur.width(3)
                tur.color('red')
                tur.fd(210)
                tur.pd()
                tur.fd(20)
                tur.up()
                tur.setpos(0,0)
                tur.rt(5)
                
                tur.width(8)
                tur.color('black')
        

    tur.setpos(0,0)
    tur.setheading(90)
    
    #for hour hand
    tur.color('green')
    tur.pd()
    tur.width(8)
    tur.right(30*h)
    tur.fd(80)
    tur.up()
    
    #minute
    tur.color('gray')
    tur.setheading(90)
    tur.width(5)
    tur.setpos(0,0)
    tur.right(6*m)
    tur.pd()
    tur.fd(110)
    tur.up()
    
    # for second hand
    tur.setheading(90)
    tur.color('cyan')
    tur.setpos(0,0)
    tur.width(3)
    tur.pd()
    tur.rt(6*s)
    tur.fd(150)
    tur.up()
    
#the loop makes it iterate and when it iterates it becomes updated...    
while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%s"))
    
    analog_clock(h,m,s)
    
    scrn.update()#updates the time
    time.sleep(1)
   
    
    tur.clear()
        
      
        
        

    
 
  
   
    
turtle.done()




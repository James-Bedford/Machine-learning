import turtle
import random
import os
import csv

head = [0]
#score
a = [0]
b = [0]
obstacle_Left = 0
obstacle_Right = 0
obstacle_Front = 0
game_continue = 's'
#food coordinates
foodcoord = [0,0,0]

#cursor position
cpos = []

def home(x,y):
    x = 0
    y=0
    a[0] = 0
    b[0] = 0
    head[0]=0
    foodcoord[2] = 0
    cpos[:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color('red')
    turtle.goto(0,0)
    turtle.write('Start',align='center',font=(15))
    turtle.title('Snake AI')
    turtle.onscreenclick(start)
    turtle.mainloop()

def window():
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(20)
    turtle.color('black')
    turtle.goto(-220,220)
    turtle.pd()
    turtle.goto(220,220)
    turtle.goto(220,-220)
    turtle.goto(-220,-220)
    turtle.goto(-220,220)
    turtle.pu()
    turtle.goto(0,0)

def start(x,y):
    turtle.onscreenclick(None)

    window()

    tfood = turtle.Turtle()
    tfood.hideturtle()
    tfood.pu()
    tfood.speed(0)
    tfood.shape('square')
    tfood.color('red')

    tscore = turtle.Turtle()
    tscore.pu()
    tscore.speed(0)
    tscore.goto(100,-250)
    tscore.write('Score: ' + str(a[0]),align='center',font=(10))

#Touch the side and die code!
    while x > -210 and x < 210 and y > -210 and y < 210:
        if foodcoord[2] ==0:
            food(tfood)
            foodcoord[2] = 1
        turtle.onkey(Up,'Up')
        turtle.onkey(Left,'Left')
        turtle.onkey(Right,'Right')
        turtle.onkey(Down,'Down')
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()
        game_continue = 'continue'
        #Add food direction indicator
        if x >foodcoord[0]:
            obstacle_Left = 1
        else:
            obstacle_Left = 0
        if y >foodcoord[1]:
            obstacle_Front = 1
        else:
            obstacle_Front = 0
        if x>foodcoord[0]:
            obstacle_Right = 1
        else:
            obstacle_Right = 0


        #End of food direction indicator
        testwritingdata(str(x),str(y),str(turtle.heading()),str(foodcoord[0]),str(foodcoord[1]),str(game_continue),str(a[0]),str(obstacle_Left))
        #Test writing data end
        if x >foodcoord[0]*20-5 and x <foodcoord[0] * 20+5 and y >foodcoord[1]*20-5 and y<foodcoord[1]*20+5:
            foodcoord[2] = 0
            tfood.clear()
            a[0]+=1
            tscore.clear()
            tscore.write('Score: ' + str(a[0]),align='center',font = (10))
        if len(cpos)>1:
            for i in range(1,len(cpos)):
                if x <cpos[i][0]+5 and x >cpos[i][0]-5 and y <cpos[i][1]+5 and y >cpos[i][1]-5:
                    tscore.clear()
                    tfood.clear()
                    game_continue = 'loss'
                    testwritingdata(str(x), str(y),str(turtle.heading()), str(foodcoord[0]), str(foodcoord[1]), str(game_continue),str(a[0]),str(obstacle_Left))
                    gameover()
                    
    tscore.clear()
    tfood.clear()
    game_continue = 'loss'
    testwritingdata(str(x), str(y),str(turtle.heading()), str(foodcoord[0]), str(foodcoord[1]),str(game_continue),str(a[0]),str(obstacle_Left))
    gameover()
    
#food
def food(tfood):
    x = random.randrange(-8,8,1)
    y = random.randrange(-8,8,1)
    foodcoord[0] = x
    foodcoord[1] = y
    tfood.hideturtle()
    tfood.pu()
    tfood.shape('square')
    tfood.color('red')
    tfood.goto(x*20,y*20)
    tfood.stamp()
#Direction keys
#Up
def Up():
    if head[0] == 270:
        pass
    else:
        head[0] = 90
#Down
def Down():
    if head[0] == 90:
        pass
    else:
        head[0] = 270
#Left
def Left():
    if head[0] == 0:
        pass
    else:
        head [0] = 180
#Right
def Right():
    if head[0] == 180:
        pass
    else:
        head[0]=0
        
def move():
    turtle.pensize(1)
    turtle.color('green')
    turtle.pu()
    turtle.speed(3)
    turtle.setheading(head[0])
    turtle.shape('square')
    turtle.stamp()
    turtle.fd(10)
    x = turtle.xcor()
    y = turtle.ycor()
    if b[0] > a[0]:
        turtle.clearstamps(1)
        cpos.insert(0,[round(x),round(y)])
        cpos.pop(-1)
    else:
        cpos.insert(0,[round(x),round(y)])
        b[0]+=1
        
def gameover():
    game_continue = 'l'
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0,150)
    turtle.color('red')
    turtle.write('Game Over',align='center',font=(15))
    turtle.goto(0,50)
    turtle.write('Score: '+ str(a[0]),align='center',font=(10))
    turtle.goto(100,100)
    turtle.write('Click to return',align='center',font=(15))
    turtle.onscreenclick(home)
    turtle.mainloop()

def testwritingdata(xco,yco,snakeheading,foodx,foody,win,sections,obstacle_L):
    learning_file = open('learning_results.csv','a')
    learning_file.writelines(xco + ',')
    learning_file.writelines(yco +',')
    learning_file.writelines(snakeheading + ',')
    learning_file.writelines(foodx *20+',')
    learning_file.writelines(foody *20 + ',')
    learning_file.writelines(win + ',')
    learning_file.writelines(sections + ',')
    learning_file.writelines(obstacle_L +'\n')
    learning_file.close()
    foodx = 0
    foody = 0


if __name__ == '__main__':
    home(0,0)
                 
                 
    
        
        
    
                 
                 
    

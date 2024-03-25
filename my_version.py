from turtle import Turtle , Screen
import random

rgb_colors=[(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220), (97, 127, 168), (34, 81, 49), (180, 188, 210), (84, 65, 30), (16, 77, 106)]

tim=Turtle()
tim.penup()
tim.hideturtle()
pos_y=-200
tim.speed(0)
for j in range(10):
    tim.setx(-250)
    tim.sety(pos_y)
    pos_y+=50
    
    for i in range (10):
        color=random.choice(rgb_colors)
        color_string = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
        
        tim.dot(20,color_string)
        tim.forward(50)




screen= Screen()
screen.exitonclick()
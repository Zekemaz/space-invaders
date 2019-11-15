#BULLET RESOURCES

import turtle
import os
import math
import random
import datetime
import Player_Resources


from Player_Resources import player

#REGISTER SHAPES

turtle.register_shape("sharingan.gif")

#CREATE THE BULLET
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("sharingan.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.2, 0.8)
bullet.hideturtle()

bulletspeed = 20
bulletstate = "ready" #Define bullet state -- ready = ready to fire -- fire = bullet is firing

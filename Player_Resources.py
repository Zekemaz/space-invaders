#PLAYER

import turtle
import os
import math
import random
import datetime


turtle.register_shape("player.gif")
#CREATE THE PLAYER
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15


#MOVE PLAYER LEFT, RIGHT, UP, DOWN
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	player.setx(x)
	
	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def move_up():
	y = player.ycor()
	y += playerspeed
	if y >= 275:
		y = 275
	player.sety(y)

def move_down():
	y = player.ycor()
	y -= playerspeed
	if y <= -250:
		y = -250
	player.sety(y)







	
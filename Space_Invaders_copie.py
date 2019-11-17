import turtle
import os
import math
import random
import datetime
import Player_Resources
import Game_Borders
import Bullet_Resources
import Enemy_Resources
from tkinter import *
from turtle import Screen, Turtle
from random import choice, randint

#SET UP WINDOW
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.setup(width=1200, height=800)
wn.bgpic("spacebg.png")
#os.system("afplay space_invaders.wav&")
#stop(os.system("afplay space_invaders.wav&"))

FONTSIZE = 12
FONT = ('Outer Space', FONTSIZE, 'normal')
turtle.penup()
turtle.setx(-520)
turtle.sety(280)

with open("spaceinvaders_score.txt") as file:
    for line in file:
        turtle.write(line.strip(), font=FONT)
        turtle.goto(turtle.xcor(), turtle.ycor() - FONTSIZE)
        turtle.color("green")

from Game_Borders import ladder_border_pen, ladder_pen, game_border_pen, space_name_pen, invader_name_pen, si2d_name_pen, score, game_score_pen, credits_border_pen, credits_pen, score
#SCORE BORDER
#SCORE IN SCORE BORDER
#GAME BORDER
#NAME ABOVE GAME BORDER
#SET SCORE TO 0 BEFORE DRAWING IT
#DRAW THE SCORE IN GAME

#PLAYER
from Player_Resources import player


from Enemy_Resources import number_of_enemies, enemy_images, enemies, enemy, enemyspeed, number_of_enemies2, enemy2_images, image2, enemies2, enemy2

#ENEMIES
#CHOOSE A NUMBER OF ENEMIES
#CREATE AN EMPTY LIST OF ENEMIES
# ADD ENEMIES TO THE LIST
# CREATE THE ENEMY

#CREATE THE BULLET
from Bullet_Resources import bullet, bulletspeed, bulletstate

from Player_Resources import move_left, move_right, move_up, move_down

def fire_bullet():
	#DECLARE BULLETSTATE AS GLOBAL IF IT NEEDS CHANGES
	global bulletstate
	if bulletstate == "ready":
		os.system("afplay laseraigu.wav&")
		bulletstate = "fire"
		#MOVE BULLET TO JUST ABOVE THE PLAYER
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

#COLLISION BULLET-ENEMY
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 25:
		return True
	else:
		return False

#CREATE KEYBOARD
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(fire_bullet, "space")



#MAIN GAME LOOP
while True:

#CHECK FOR COLLISION BETWEEN PLAYER-ENEMY
	if isCollision(player, enemy):
		os.system("afplay Laugh.wav&")
		player.hideturtle()
		break
	# if isCollision(player, enemy):
	# 	os.system("afplay space_invaders.wav&")
	
	#MOVE BULLET
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y) 

	
	#CHECK IF BULLET HAS GONE TO TOP
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"

	#MOVE THE ENEMY
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
	
		#MOVE ENEMY BACK AND DOWN
		if enemy.xcor() > 280:
			#MOVE ALL ENEMIES DOWN
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			#MOVE ENEMIES DOWN
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
				#CHANGE ENEMY DIRECTION
			enemyspeed *= -1


		#CHECK COLLISION BULLET-ENEMY
		if isCollision(bullet, enemy):
			os.system("afplay explosion.wav&")
			
			#RESET BULLET
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)

			#RESET ENEMY
			x = randint(-200, 200)
			y = randint(100, 250)
			enemy.setposition(x,y)

			#UPDATE SCORE
			score += 100
			scorestring = "Score %s" %score
			scorestring2 = "%s" %score
			game_score_pen.clear()
			game_score_pen.write(scorestring, False, align="left", font=("Arial", 17, "normal"))

		#UPDATE SCOREBOARD AT DEATH
		if isCollision(player, enemy):
			text = wn.textinput("Ladder", "Enter your Initials: ")
			with open("spaceinvaders_score.txt","a") as f:
				f.write(text + " -- %s\r\n\n" % scorestring2)
				print()
			break

	#MOVE THE ENEMY2
	for enemy2 in enemies2:
		x = enemy2.xcor()
		x += enemyspeed
		enemy2.setx(x)

		#MOVE ENEMY2 BACK AND DOWN
		if enemy2.xcor() > 280:
			#MOVE ALL ENEMIES DOWN
			for e in enemies2:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#CHANGE ENEMY2 DIRECTION
			enemyspeed *= -1

		if enemy2.xcor() < -280:
			#MOVE ENEMIES2 DOWN
			for e in enemies2:
				y = e.ycor()
				y -= 40
				e.sety(y)
				#CHANGE ENEMY2 DIRECTION
			enemyspeed *= -1

		#CHECK COLLISION BULLET-ENEMY2
		if isCollision(bullet, enemy2):
			os.system("afplay explosion.wav&")
			
			#RESET BULLET
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)

			#RESET ENEMY2
			x = randint(-200, 200)
			y = randint(100, 250)
			enemy2.setposition(x,y)

		
			#UPDATE SCORE
			score += 100
			scorestring = "Score %s" %score
			scorestring2 = "%s" %score
			game_score_pen.clear()
			game_score_pen.write(scorestring, False, align="left", font=("Arial", 17, "normal"))
		
		#UPDATE SCOREBOARD AT DEATH
		if isCollision(player, enemy2):
			text = wn.textinput("Ladder", "Enter your Initials: ")
			with open("spaceinvaders_score.txt","a") as f:
				f.write(text + " -- %s\r\n\n" % scorestring2)
				print()
			break




while True:
	wn.update()

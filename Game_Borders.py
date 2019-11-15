#Thanks to Christian Thompson for the tutorial

#SCORE AND GAME BORDERS AND TITLES + DRAW SCORE IN GAME


import turtle
import os
import math
import random
import datetime
from tkinter import *
from turtle import Screen, Turtle
from random import choice, randint

#f= open("spaceinvaders_score.txt","a")
#SCORE BORDER
ladder_border_pen = turtle.Turtle()
ladder_border_pen.speed(0)
ladder_border_pen.color("white")
ladder_border_pen.penup()
ladder_border_pen.setposition(-530, -300)
ladder_border_pen.pendown()
ladder_border_pen.pensize(3)
for side in range(4):
    ladder_border_pen.fd(200)
    ladder_border_pen.lt(90)
    ladder_border_pen.fd(600)
    ladder_border_pen.lt(90)
ladder_border_pen.hideturtle()

#LADDER ABOVE SCORE BORDER
ladder_pen = turtle.Turtle()
ladder_pen.speed(0)
ladder_pen.color("yellow")
ladder_pen.penup()
ladder_pen.setposition(-515, 303)
scoreboard = "LADDER"
ladder_pen.write(scoreboard, False, align="Left", font=("Outer Space", 26 , "normal"))
ladder_pen.hideturtle()

"""ladder_score_pen = turtle.Turtle()
ladder_score_pen.speed(0)
ladder_score_pen.color("purple")
ladder_score_pen.penup()
ladder_score_pen.setposition(333, 303)
contents = f.t()
ladder_score_pen.write(contents, False, align="Left", font=("Outer Space", 26 , "normal"))
ladder_score_pen.hideturtle()"""

#GAME BORDER
game_border_pen = turtle.Turtle()
game_border_pen.speed(0)
game_border_pen.color("white")
game_border_pen.penup()
game_border_pen.setposition(-300, -300)
game_border_pen.pendown()
game_border_pen.pensize(3)
for side in range(4):
    game_border_pen.fd(600)
    game_border_pen.lt(90)
game_border_pen.hideturtle()

#NAME ABOVE GAME BORDER
space_name_pen = turtle.Turtle()
space_name_pen.speed(0)
space_name_pen.color("red")
space_name_pen.penup()
space_name_pen.setposition(-250, 303)
space_name = "Space "
space_name_pen.write(space_name, False, align="Left", font=("Outer Space", 27 , "normal"))
space_name_pen.hideturtle()

invader_name_pen = turtle.Turtle()
invader_name_pen.speed(0)
invader_name_pen.color("blue")
invader_name_pen.penup()
invader_name_pen.setposition(-75, 303)
invader_name = "Invaders "
invader_name_pen.write(invader_name, False, align="Left", font=("Outer Space", 27 , "normal"))
invader_name_pen.hideturtle()

si2d_name_pen = turtle.Turtle()
si2d_name_pen.speed(0)
si2d_name_pen.color("green")
si2d_name_pen.penup()
si2d_name_pen.setposition(220, 303)
si2d_name = "2D"
si2d_name_pen.write(si2d_name, False, align="Center", font=("Outer Space", 27 , "normal"))
si2d_name_pen.hideturtle()

#SET SCORE TO 0 BEFORE DRAWING IT
score = 0

#DRAW THE SCORE IN GAME
game_score_pen = turtle.Turtle()
game_score_pen.speed(0)
game_score_pen.color("white")
game_score_pen.penup()
game_score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
game_score_pen.write(scorestring, False, align="left", font=("Arial", 17, "normal"))
game_score_pen.hideturtle()

#CREDITS
credits_border_pen = turtle.Turtle()
credits_border_pen.speed(0)
credits_border_pen.color("white")
credits_border_pen.penup()
credits_border_pen.setposition(330, -300)
credits_border_pen.pendown()
credits_border_pen.pensize(3)
for side in range(4):
    credits_border_pen.fd(200)
    credits_border_pen.lt(90)
    credits_border_pen.fd(600)
    credits_border_pen.lt(90)
credits_border_pen.hideturtle()

#CREDITS ABOVE CREDITS BORDER
credits_pen = turtle.Turtle()
credits_pen.speed(0)
credits_pen.color("purple")
credits_pen.penup()
credits_pen.setposition(333, 303)
credits = "CREDITS"
credits_pen.write(credits, False, align="Left", font=("Outer Space", 26 , "normal"))
credits_pen.hideturtle()

#CREDITS
credits_filling_pen = turtle.Turtle()
credits_filling_pen.speed(0)
credits_filling_pen.color("yellow")
credits_filling_pen.penup()
credits_filling_pen.setposition(334, -40)
credits = "Graphics\r\r\r\r\rSounds FX\r\r\r\r\r\r\r\r\rHelp"
credits_filling_pen.write(credits, False, align="Left", font=("Outer Space", 18 , "normal"))
credits_filling_pen.hideturtle()

credits1_filling_pen = turtle.Turtle()
credits1_filling_pen.speed(0)
credits1_filling_pen.color("blue")
credits1_filling_pen.penup()
credits1_filling_pen.setposition(333, 40)
credits1 = "Colors\r\r\r\r\r\r\rLaser Snd\r\r\rExplosion Snd\r\r\rGame Over Snd"
credits1_filling_pen.write(credits1, False, align="Left", font=("Outer Space", 13 , "normal"))
credits1_filling_pen.hideturtle()

credits2_filling_pen = turtle.Turtle()
credits2_filling_pen.speed(0)
credits2_filling_pen.color("red")
credits2_filling_pen.penup()
credits2_filling_pen.setposition(333, 20)
credits2 = " Gabriel Dessere\r\r\r\r\r\r\r\r\r\r\r Thomas C.\r\r\r\r\r Sebastien X.C.\r\r\r\r\r Sebastien X.C."
credits2_filling_pen.write(credits2, False, align="Left", font=("Outer Space", 8 , "normal"))
credits2_filling_pen.hideturtle()

credits3_filling_pen = turtle.Turtle()
credits3_filling_pen.speed(0)
credits3_filling_pen.color("red")
credits3_filling_pen.penup()
credits3_filling_pen.setposition(333, -125)
credits3 = " Mathieu Ducournau\r Clement Lecram\r Sebastien X.C\r Thomas Corno\r Glenn Oberle\r Maxime RIL\r Israel Kabran"
credits3_filling_pen.write(credits3, False, align="Left", font=("Outer Space", 8 , "normal"))
credits3_filling_pen.hideturtle()





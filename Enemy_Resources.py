#ENEMY RESOURCES
import turtle
import os
import math
import random
import datetime
from tkinter import *
from turtle import Screen, Turtle
from random import choice, randint


#ENEMIES
#CHOOSE A NUMBER OF ENEMIES
number_of_enemies = 5

enemy_images = ["1.gif", "2.gif", "3.gif", "4.gif"]

for image in enemy_images:
    turtle.register_shape(image)

# CREATE AN EMPTY LIST OF ENEMIES
enemies = []

# ADD ENEMIES TO THE LIST
for _ in range(number_of_enemies):

    # CREATE THE ENEMY
    enemy = Turtle(shape=choice(enemy_images), visible=False)
    enemy.speed('fastest')
    enemy.penup()
    x = randint(-200, 200)
    y = randint(100, 250)
    enemy.setposition(x, y)
    enemy.showturtle()

    enemies.append(enemy)
enemyspeed = 2
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
number_of_enemies = 4

enemy_images = ["1_1.gif", "1_2.gif", "1_3.gif", "1_4.gif"]

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



#ENEMY2
#CHOOSE A NUMBER OF ENEMY2
number_of_enemies2 = 4

enemy2_images = ["4.gif"]

for image2 in enemy2_images:
    turtle.register_shape(image2)

# CREATE AN EMPTY LIST OF ENEMIES
enemies2 = []

# ADD ENEMIES TO THE LIST
for _ in range(number_of_enemies2):

    # CREATE THE ENEMY
    enemy2 = Turtle(shape=choice(enemy2_images), visible=False)
    enemy2.speed('fastest')
    enemy2.penup()
    x = randint(-200, 200)
    y = randint(100, 250)
    enemy2.setposition(x, y)
    enemy2.showturtle()

    enemies.append(enemy2)
enemyspeed = 2




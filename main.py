import pygame
import tkinter as tk
import sys
import math
from pygame.locals import *
from tkinter import *


pygame.init()
running = True


#pygame display set up
screenSize = (1280, 720) #is this a good size, or 720p better?
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
pygame.display.set_caption("IPOMS")

#tkinter settings screen set up
root = tk.Tk() # create a Tk root window
w = 720 #width
h = 320 #height

#def orbit variables:
r = 320 #radius of orbit [user input]
t = 0 #tickrate (milliseconds)
T = 5 #period of orbit - [calculated] via eqn using user input for other values
M = 10 #[user input]
m = 10 #[user input]


#display loop
while running == True:
    t = pygame.time.get_ticks()/1000
    screen.fill((255,255,255)) #maybe create toggle light vs dark mode

    #Quitting the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Full screening the simulation
        # if event.type == 

    #Settings menu (Located top right of the program), which includes options such as changing variables, and includes formulae values and information about the orbit/s
        # if event.type == KEYDOWN:
            # if event.key == K_ESCAPE:
                

    #resizing the window: [DO WE WANT IT SCALABLE? it might mess with our program...]
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    pygame.draw.circle(screen, [0, 0, 0, 255], (480, 360), 40) #replace 40 with "M"
    pygame.draw.circle(screen, [0, 0, 0, 255], (480+r*math.cos(t*2*math.pi/T),360+r*math.sin(t*2*math.pi/T)), 30) #(480, 360) is centre of the LHS screen

    pygame.display.update()


#drawing a circle - idk why its not coming up; smth wrong with the numbers?


#planet class

# class Planet()



#settings menu






#Hey, Sam, if we get this to work, we could build more simulations ahahaha.. could even make a website to collate them; but im probs being too ambitious rn LOL
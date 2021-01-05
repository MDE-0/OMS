import pygame
import tkinter
import sys
import math
from pygame.locals import *
from tkinter import *
from random import randint

pygame.init()
running = True


#pygame display set up
screenSize = (1280, 720) #is this a good size, or 720p better?
menuSize = (320, screenSize[1])
simSize = (screenSize[0] - menuSize[0], screenSize[1])
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
pygame.display.set_caption("IPOMS")



#def orbit variables:
r = 320 #radius of orbit [user input]
t = 0 #tickrate (milliseconds)
T_calculated = 500000 #[calculated] via eqn using user input for other values
T = T_calculated/100000 #period of orbit (perhaps x10^5 or smth, as otherwise it would be super) 
M = 10 #[user input]
m = 10 #[user input]

stars = []

def genStars():
    for i in range(150):
        stars.append((randint(0, simSize[0]), randint(0, simSize[1])))

genStars()

#display loop
while running == True:
    t = pygame.time.get_ticks()/1000
    #maybe create toggle light vs dark mode

    #Quitting the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            exit()

    #Full screening the simulation
        # if event.type == 

    #Settings menu (Located top right of the program), which includes options such as changing variables, and includes formulae values and information about the orbit/s
        # if event.type == KEYDOWN:
            # if event.key == K_ESCAPE:
                

    #resizing the window: [DO WE WANT IT SCALABLE? it might mess with our program...]
        if event.type == VIDEORESIZE:
            screenSize = (event.w,event.h)
            menuSize = (menuSize[0],event.h)
            simSize = (screenSize[0] - menuSize[0], screenSize[1])
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            stars = []
            genStars()
    

    
    simSurface = pygame.Surface((screenSize[0]-menuSize[0],screenSize[1]))
    menuSurface = pygame.Surface(menuSize)


    


    simSurface.fill((0,0,0))
    menuSurface.fill((125,125,125,125)) 
    for i in range(150):
        pygame.draw.circle(simSurface, (255,255,255), stars[i], 1)  
    centre = (simSize[0]/2,simSize[1]/2)
    rad = simSize[0]/5
    for baseAngle in range(0, 2*math.floor(math.pi*1000), 40):
        angle = baseAngle/1000
        pygame.draw.circle(simSurface, [0,0,0,255],(centre[0] + rad*math.cos(angle),centre[1] + rad*math.sin(angle)),2)
    pygame.draw.circle(simSurface, [187,187,187, 255], (centre[0] + rad*math.cos(t), centre[1]+rad*math.sin(t)), 30)
    pygame.draw.circle(simSurface, [30,30,255, 255], centre, 40)
    pygame.draw.line(simSurface, [255, 255, 255, 255], (centre[0] + rad*math.cos(t), centre[1]+rad*math.sin(t)), centre, width = 3)


    screen.blit(simSurface,(0,0))
    screen.blit(menuSurface,(screenSize[0]-menuSize[0],0))

    pygame.display.update()

#planet class

# class Planet()



#settings menu






#Hey, Sam, if we get this to work, we could build more simulations ahahaha.. could even make a website to collate them; but im probs being too ambitious rn LOL
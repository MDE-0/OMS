import pygame
import tkinter
import sys
from pygame.locals import *
from tkinter import *


pygame.init()
running = True


#pygame display set up
screenSize = (1280, 720) #is this a good size, or 720p better?
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
pygame.display.set_caption("IPOMS")


#display loop
while running == True:

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
    

    
    pygame.display.update()


#drawing a circle - idk why its not coming up; smth wrong with the numbers?
pygame.draw.circle(screen, [255, 255, 255, 255], (500, 500), 100)

#planet class

# class Planet()



#settings menu






#Hey, Sam, if we get this to work, we could build more simulations ahahaha.. could even make a website to collate them; but im probs being too ambitious rn LOL
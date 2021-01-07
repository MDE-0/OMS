import pygame
import pygame_gui
import sys
import math
from pygame.locals import *

from random import randint

pygame.init()
running = True


#pygame display set up
screenSize = (1280, 720) #is this a good size, or 1080p better?
menuSize = (320, screenSize[1])
simSize = (screenSize[0] - menuSize[0], screenSize[1])
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
pygame.display.set_caption("Interactive Physics Orbital Mechanics Simulation (IPOMS)")
screen.fill((0, 0, 0))

#Python GUI menu
manager = pygame_gui.UIManager(screenSize)
clock = pygame.time.Clock()


#def orbit variables:
vars = {
    'r' : ["Radius [R(m)]",320],#radius of orbit [user input]
    'M' : ["M mass [M(kg)]",10], #[user input]
    'm' : ["m mass [m(kg)]",10], #[user input]
}
t = 0 #tickrate (milliseconds)
T_calculated = ["Period [T(s)]",500000] #[calculated] via eqn using user input for other values
T = T_calculated[1]/100000 #period of orbit (perhaps x10^5 or smth, as otherwise it would be super) 
stars = []

def genStars():
    for i in range(100):
        stars.append((randint(0, simSize[0]), randint(0, simSize[1])))

class button(object):
    def __init__(self, var, y_placement):
        self.var = var
        self.y_placement = y_placement
        self.var_name = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0] + 0,y_placement*50), (120, 50)), text = f"{vars[self.var][0]}", manager = manager)
        self.increase = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0] + 120,y_placement*50), (50, 50)), text = "↑", manager = manager)
        self.decrease = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0] + 170, y_placement*50), (50, 50)), text = "↓", manager = manager)
        self.value = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0] + 220, y_placement*50), (100, 50)), text = f"{vars[self.var][1]}", manager = manager)
        
            
ind = 0
buttons = []
for name in vars:
    list.append(buttons, button(name, ind))
    ind = ind + 1





genStars()

#display loop
while running == True:
    time_delta = clock.tick(144)/1000.0
    t = pygame.time.get_ticks()/1000
    #maybe create toggle light vs dark mode

    #Quitting the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            exit()
       
        elif event.type == VIDEORESIZE:
            screenSize = (event.w,event.h)
            menuSize = (menuSize[0],event.h)
            simSize = (screenSize[0] - menuSize[0], screenSize[1])
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            stars = []
            genStars()
        elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            for but in buttons:
                if event.ui_element == but.increase: 
                    vars[but.var][1] += 5
                    but.value.kill()
                    but.value = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0] + 220, but.y_placement*50), (100, 50)), text = f"{vars[but.var][1]}", manager = manager)
                elif event.ui_element == but.decrease:
                    vars[but.var][1] -= 5
                    but.value.text = f"{vars[but.var][1]}"
                    but.value.kill()
                    but.value = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((simSize[0] + 220, but.y_placement*50), (100, 50)), text = f"{vars[but.var][1]}", manager = manager)
        manager.process_events(event)
    
    
    
    
    simSurface = pygame.Surface((screenSize[0]-menuSize[0],screenSize[1]))
 


    screen.fill((200,200,200,200))
    simSurface.fill((0,0,0))
    
    
    


    for i in range(100):
        pygame.draw.circle(simSurface, (255,255,255), stars[i], 1)  
    
    centre = (simSize[0]/2,simSize[1]/2)


    radius_planet = 40
    radius_satellite = 30
    for baseAngle in range(0, 2*math.floor(math.pi*1000), 40):
        angle = baseAngle/1000
        pygame.draw.circle(simSurface, [173,255,47,255],(centre[0] + vars["r"][1]*math.cos(angle),centre[1] + vars["r"][1]*math.sin(angle)), 1)

    #draw_arrow function

    def draw_arrow(screen, colour, start, end):
        pygame.draw.line(screen,colour,start,end,2)
        rotation = math.degrees(math.atan2(start[1]-end[1], end[0]-start[0]))+90
        pygame.draw.polygon(screen, colour, ((end[0]+5*math.sin(math.radians(rotation)), end[1]+5*math.cos(math.radians(rotation))), (end[0]+5*math.sin(math.radians(rotation-120)), end[1]+5*math.cos(math.radians(rotation-120))), (end[0]+5*math.sin(math.radians(rotation+120)), end[1]+5*math.cos(math.radians(rotation+120)))))
    setattr(pygame.draw, "arrow", draw_arrow)

    
    pygame.draw.circle(simSurface, [30,30,255, 255], centre, radius_planet)

    
    #BELOW FUNCTION WORKS WITH draw_arrow function
    pygame.draw.arrow(simSurface, [255, 255, 255, 255], (centre[0] + vars["r"][1]*math.cos(t), centre[1]+vars["r"][1]*math.sin(t)), (centre[0] + radius_planet*math.cos(t), centre[1]+radius_planet*math.sin(t)))
    
    offsetAngle = 0.5
    pygame.draw.arrow(simSurface, [255, 255, 255, 255], (centre[0] + vars["r"][1]*math.cos(t), centre[1]+vars["r"][1]*math.sin(t)), (centre[0] + vars["r"][1]*1/math.cos(offsetAngle)*math.cos(t + offsetAngle), centre[1] + vars["r"][1]*1/math.cos(offsetAngle)*math.sin(t + offsetAngle)))
    ### WHEN F_g BUTTON COMES INTO CONTACT WITH MOUSE POINTER, CHANGE COLOUR OF ARROW (HIGHLIGHTING EFEFCT)

    pygame.draw.circle(simSurface, [187,187,187, 255], (centre[0] + vars["r"][1]*math.cos(t), centre[1]+vars["r"][1]*math.sin(t)), radius_satellite)
    
    
    #defining buttons
    





    

    

    #I'm not sure why this isn't working....
    screen.blit(simSurface,(0,0))
    manager.draw_ui(screen)
    

    # manager.set_visual_debug_mode(True)
    

    
    pygame.display.update()
    manager.update(time_delta)


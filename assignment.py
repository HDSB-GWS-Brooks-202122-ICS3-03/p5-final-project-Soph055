#-----------------------------------------------------------------------------
# Name:        Zombie OutCry (assignment.py)
# Purpose:     A description of your program goes here.
#
# Author:      Mr. Brooks
# Created:     7-May-2021
# Updated:    
#-----------------------------------------------------------------------------
#I think this project deserves a level XXXXXX because ...
#
#Features Added:
#   ...
#   ...
#   ...
#-----------------------------------------------------------------------------

import pygame
import ctypes
import math
import random
from pygame import mixer
import copy

ctypes.windll.user32.SetProcessDPIAware()

class Player():
    def __init__(self):
        
        self.image = pygame.image.load("images/man.png") # loads image on player
        self.rect = [34,150, 112,62] # creates rect (points of on paint)
        self.pos = (100,700) # position
        self.speed = 1 #player speed 
        self.direction = "Right" # direction
        self.move = False # player cannot move initially
        
        # image animation variables
        self.origImageRect = copy.copy(self.rect)
        self.patchNum = 0
        self.numPatches = 6
        self.frameCount = 0
        self.animationFrameRate = 10
        
       
    
        
    def draw(self, screen): # draws player using values above
        tempSurface = pygame.Surface( (self.rect[2], self.rect[3]) ) #Makes a temp Surface using the width and height of the rect
        tempSurface.fill((1,255,1))             # makes black background colour for temp surface
        tempSurface.set_colorkey((1,255,1))     #Set the color black to be transparent
        tempSurface.blit(self.image, (0,0),  self.rect) # on temp surface draws image
        
        if self.direction == "Left":
            tempSurface = pygame.transform.flip(tempSurface,True,False) # flips horizontally but not vertically
        screen.blit(tempSurface, self.pos)
        
    

def main():
    #-----------------------------Setup------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 800   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    frameRate = 10
    screen = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    player = Player()
    
    #-----------------------------Main Game Loop----------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   # leave game loop
        elif ev.type == pygame.KEYDOWN:          
            if ev.key == pygame.K_a or pygame.KEY_LEFT:
                playerDirection = 'Left'
                playerMove = True
            elif ev.key == pygame.K_d or pygame.KEY_RIGHT:
                playerDirection = 'Right'
                playerMove = True
            elif ev.key == pygame.K_w or pygame.KEY_UP:
                playerDirection = "Up"
                playerMove = True
            elif ev.key == pygame.K_s or pygame.KEY_DOWN:
                playerDirection = "Down"
                playerMove = True    
        elif ev.type == pygame.KEYUP:
            PlayerMove = False
  #----------------------Draw all the images----------------------------#
            
        screen.fill((100,0,50))
        
        player.draw(screen)
        pygame.display.flip()
        
        clock.tick(frameRate) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
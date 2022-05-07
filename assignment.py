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



def main():
    #-----------------------------Setup------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 800   # Desired physical surface size, in pixels.
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    
    screen = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    frameCount = 0
    
    playerImage = pygame.image.load("images/man.png") # loads image on player
    
    playerImage = pygame.transform.scale2x(playerImage) # images 2x bigger

    
    
    
    playerMove = False
    playerPos = [100, 670]
    
    playerRect = [68,300, 224, 124] # image rect from paint
    
    patchNumber = 0         #Start at the initial patch
    numPatches = 6       # 6 patches
    playerFrameCount = 0          #Start at intial frame
    playerFrameRate = 10         #How often to re-draw the lizard
    playerDirection = "Right" # player intital direction
    playerSpeed = 0.5 # speed
    
    playerMove = False
    
   
    
    
    #-----------------------------Main Game Loop----------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   # leave game loop
        elif ev.type == pygame.KEYDOWN:          
            if ev.key == pygame.K_a or ev.key == pygame.K_LEFT:
                playerDirection = "Left"
                playerMove = True
            elif ev.key == pygame.K_d or ev.key == pygame.K_RIGHT:
                playerDirection = "Right"
                playerMove = True 
        elif ev.type == pygame.KEYUP:
            playerMove = False
            
        if (playerMove):
            
            if playerDirection == "Right": # if moving right
                playerPos[0] += playerSpeed
            else:
                playerPos[0] -= playerSpeed
                
            if (frameCount % playerFrameRate == 0):    #Only change the animation frame once every 10 frames
                if (patchNumber < numPatches-1) :
                    patchNumber += 1
                    playerRect[0] += playerRect[2]  #Shifts the "display window" to the right along the man.png sheet by the width of the image
                else:
                    patchNumber = 0           #Reset back to first patch
                    playerRect[0] -= playerRect[2]*(numPatches-1)  #Reset the rect position of the rect back too
                
            print(f"Patch Number: {patchNumber}   Image Rect: {playerRect}  ")
  #----------------------Draw all the images----------------------------#
        screen.fill((100,0,50)) 
        
        tempSurface = pygame.Surface( (playerRect[2], playerRect[3]) ) #Makes a temp Surface using the width and height of the rect
        tempSurface.fill((1,255,1))             # makes black background colour for temp surface
        tempSurface.set_colorkey((1,255,1))     #Set the color black to be transparent
        tempSurface.blit(playerImage, (0,0), playerRect) # on temp surface draws image
        
        if playerDirection == "Left":
            tempSurface = pygame.transform.flip(tempSurface,True,False) # flips horizontally but not vertically
        screen.blit(tempSurface, playerPos)
        
        
        

      
        
        pygame.display.flip()
        
        frameCount += 1
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()
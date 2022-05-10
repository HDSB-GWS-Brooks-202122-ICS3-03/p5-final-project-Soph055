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

# a list with images of zombie walking
zombWalk =[pygame.image.load("images\Walk_1.png"),pygame.image.load("images\Walk_2.png"),
           pygame.image.load("images\Walk_3.png"),pygame.image.load("images\Walk_4.png"),
           pygame.image.load("images\Walk_5.png"),pygame.image.load("images\Walk_6.png"),
           pygame.image.load("images\Walk_7.png"),pygame.image.load("images\Walk_8.png"),
           pygame.image.load("images\Walk_9.png"),pygame.image.load("images\Walk_10.png")]


class Player(): # player class
    def __init__(self):
        
        self.image = pygame.image.load("images/man.png") # loads image of player
        self.rect = [34,150, 112,62] # creates rect (points from paint)
        self.pos = [100,510] # position
        self.speed = 1 #player speed 
        self.direction = "Right" # direction
        self.move = False # player cannot move initially
        
        # image animation variables
        self.patchNumber = 0 # intial patch number
        self.numPatches = 6 # number of patches to go through
        self.FrameRate = 10 # frame rate for player animation
    
    def walk (self):
        if (self.move): # if player can move 
            if self.direction == "Right": # if moving right
                self.pos[0] += self.speed # move right on x axis
            else: # if moving left..
                self.pos[0] -= self.speed #moves left on x axis
        
    def draw(self, screen): # draws player 
        tempSurface = pygame.Surface( (self.rect[2], self.rect[3]) ) #Makes a temp Surface using the width and height of the rect
        tempSurface.fill((1,255,1))             # makes black background colour for temp surface
        tempSurface.set_colorkey((1,255,1))     #Set the color black to be transparent
        tempSurface.blit(self.image, (0,0),  self.rect) # on temp surface draws image
        
        if self.direction == "Left":
            tempSurface = pygame.transform.flip(tempSurface,True,False) # flips horizontally but not vertically
        screen.blit(tempSurface, self.pos) # draws screen

class Zombie():
    def __init__(self,xPos,yPos,speed):
        
        self.rect = [0,0,521,576] # rect of image, from paint
        self.pos = [xPos,yPos] # sets y and x coords to number inputted when creating zombie
        self.speed = speed # sets speed to inputed speed
        self.move = True # zombie is moving is true
        self.moveFrame = 0 # represents which number of frame from list will be shown 
#         self.image = pygame.transform.scale2x(self.image) # makes sprite 2x bigger
        
        # image animation variables
        self.frameRate = 10 # frame rate for animation
        self.frameCount = 0
        
    def walk(self,screen):
        if self.move == True: # if zombie is moving 
            self.image = zombWalk[self.moveFrame] # draws certain image from list depending on number that moveframe is at the time
            self.pos[0] -= self.speed # makes zombie move left
            scale = 0.5
            self.image = pygame.transform.smoothscale(screen,(scale*521,scale*576))
            
            
    def update(self):
       if self.moveFrame > 8: # if moveframe is greater than 8, sets back to 0 
           self.moveFrame = 0
       elif (self.frameCount % self.frameRate == 0): # only change animtion once every 10 frames
            self.moveFrame += 1 # adds 1 to move frame 
            return ###why is this needed not sure???? still works without djfsjfl 
        
    def draw(self, screen): # draws zombie
       
        tempSurface = pygame.Surface( (self.rect[2], self.rect[3]) ) #Makes a temp Surface using the width and height of the rect
        tempSurface.fill((255,255,255))             # makes black background colour for temp surface
        tempSurface.set_colorkey((255,255,255))     #Set the color black to be transparent
        tempSurface.blit(self.image, (0,0),  self.rect) # on temp surface draws image
        screen.blit(tempSurface, self.pos) # draws screen


class Background(): # background screens class
    def __init__(self, Image, xPos, yPos): # object variables
        self.image = Image # self image is set to whatever image inputed when creating object
        self.pos = [xPos, yPos] # self position is set to number inputed from object variable  ####FIX THIS COMMENT DONT FORGET YAYAYAYYA
        
    def draw(self,screen): 
        screen.blit(self.image, self.pos) #draws screen 
    
    
    
    
    
    
def main():
    #-----------------------------Setup------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 800   # Desired physical surface size, in pixels.
    surfaceSize2 = 600
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    screen = pygame.display.set_mode((surfaceSize, surfaceSize2)) # creates screen
    pygame.display.set_caption("Zombie OutCry") # sets caption of screen
    
    frameCount = 0 # keep track of frames
    
    zombie = Zombie(700,400,0.5) # creates zombie from zombie class
    player = Player() # creates player from Playerclass

    gameScreen = Background(pygame.image.load("images/gamescreen.png"),0,0) # creates gamescreen from background class using information inputted

   
    
    
    #-----------------------------Main Game Loop----------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   # leave game loop
        elif ev.type == pygame.KEYDOWN:          # if key down..
            if ev.key == pygame.K_a or ev.key == pygame.K_LEFT: # if pressing left key/a..
                player.direction = "Left" # sets direction to left
                player.move = True # sets movement to true
            elif ev.key == pygame.K_d or ev.key == pygame.K_RIGHT: # if pressing right key/d
                player.direction = "Right" # sets direction to right
                player.move = True #sets movement to true
        elif ev.type == pygame.KEYUP: # if key up...
            player.move = False # sets movement to false
            
            
            
            
   #----------------------Game Logic Goes After Here----------------------------#           
        if player.move == True: # if player can move           
            if (frameCount % player.FrameRate == 0):    #Only change the animation frame once every 10 frames
                if (player.patchNumber < player.numPatches-1) :
                    player.patchNumber += 1
                    player.rect[0] += player.rect[2]  #Shifts the "display window" to the right along the man.png sheet by the width of the image
                else:
                    player.patchNumber = 0           #Reset back to first patch
                    player.rect[0] -= player.rect[2]*(player.numPatches-1)  #Reset the rect position of the rect back too
        elif player.move == False:# if player cannot move, set to patch 4 so it looks like man is standing straight
            player.patchNumber = 4
            player.rect =[448,150, 112,62] 
                
            print(f"Patch Number: {player.patchNumber}   Image Rect: {player.rect}  ")
            
  #----------------------Draw all the images----------------------------#
        gameScreen.draw(screen)
        player.draw(screen)
        player.walk()

        zombie.walk(screen)
        zombie.update()
        zombie.draw(screen)
        pygame.display.flip()
        
        zombie.frameCount += 1 #adds one every tick # NOT 100 PERCENT SURE
        frameCount += 1 # adds one every tick
        clock.tick(60) #Force frame rate to be slower

    pygame.quit()     # Once we leave the loop, close the window.

main()

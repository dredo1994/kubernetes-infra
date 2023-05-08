import pygame
from pygame.locals import *
import sys
import random

## Define Constants
BLACK = (0,0,0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
xspeed = 3
yspeed = 3

## Initializing the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()



## Load assets: images(s) etc
ballImage = pygame.image.load('images/ball.png')



## Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)

## Loop forever
while True:
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()




  if (ballRect.left < 0) or (ballRect.left >= MAX_WIDTH):
    xspeed = -xspeed
  if (ballRect.top < 0) or (ballRect.top >= MAX_HEIGHT):
    yspeed = -yspeed


  ballRect.left +=  xspeed
  ballRect.top +=  yspeed


  #Clear the window
  window.fill(BLACK)

  # Draw all the window elements
  window.blit(ballImage,ballRect)


  # update the window
  pygame.display.update()

  # SLow things down a bit
  clock.tick(FRAMES_PER_SECOND)

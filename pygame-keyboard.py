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
MAX_WIDTH  = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X=400
TARGET_Y=320
TARGET_WIDTH_HEIGHT=120

## Initializing the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()



## Load assets: images(s) etc
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.jpg')



## Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X,TARGET_Y,TARGET_WIDTH_HEIGHT,TARGET_WIDTH_HEIGHT)


## Loop forever
while True:
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

     # see if the user clicked
     if event.type == pygame.KEYDOWN:
        ## Move the ball image based on the type of key press
        if event.key == pygame.K_LEFT:
           ballX = ballX - 3
        if event.key == pygame.K_RIGHT:
           ballX = ballX + 3
        if event.key == pygame.K_DOWN:
           ballY = ballY + 3
        if event.key == pygame.K_UP:
           ballY = ballY - 3

  ## Check if ball is colliding with  the target
  ballRect = pygame.Rect(ballX,ballY,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)
  if ballRect.colliderect(targetRect):
     print("Ball id inside the target")



  #Clear the window
  window.fill(BLACK)

  # Draw all the window elements
  window.blit(targetImage,(TARGET_X,TARGET_Y))
  window.blit(ballImage, (ballX,ballY))


  # update the window
  pygame.display.update()

  # SLow things down a bit
  clock.tick(FRAMES_PER_SECOND)

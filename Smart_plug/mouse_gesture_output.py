import pygame, random, sys
from pygame.locals import *
import mouse_gesture

width = 600
height = 600
FPS = 10

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test window')

points = []
mouseDown = False
font = pygame.font.SysFont(None, 24)
strokeText = ''

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if len(points) > 2:
            startx, starty = points[0][0], points[0][1]
            for i in range(len(points)):
                points[i] = (points[i][0] - startx, points[i][1] - starty)
        strokes = mouse_gesture.getGesture(points)
        strokeText = mouse_gesture.getGestureStr(strokes)
        
        if not strokeText:
            print 'No direction'
            strokeText=[]
        else:
            gesture=len(strokeText)-1
            print strokeText[gesture]

        if event.type == MOUSEMOTION:
            points.append( (event.pos[0], event.pos[1]) )
        else:
            points=[]

    pygame.display.update()
    mainClock.tick(FPS)
    
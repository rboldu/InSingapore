import pygame, random, sys
from pygame.locals import *
import mouse_gesture
from Queue import Queue
from ComandList import *
from threading import Thread

width = 600
height = 600
FPS = 1

Co_MOUSE_UP=Co_Increase
Co_MOUSE_DOWN=Co_Decrease
Co_MOUSE_RIGHT=Co_Parameter_Increase
Co_MOUSE_LEFT=Co_Parameter_Decrease

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test window')

points = []
mouseDown = False
font = pygame.font.SysFont(None, 24)
strokeText = ''

gesture=0
last=0
check='S'

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
            last=0
        else:

            gesture=len(strokeText)-1
            key=strokeText[gesture]
            if(key=='U' and check!='U'):
                print 'up'
                check='U'
                #self.q.put([self.id,Co_MOUSE_UP,100])
            elif(key=='D'and check!='D'):
                print 'down'
                check='D'
                #self.q.put([self.id,Co_MOUSE_DOWN,100])
            elif(key=='R'and check!='R'):
                print 'right'
                check='R'
                #self.q.put([self.id,Co_MOUSE_RIGHT,100])
            elif(key=='L'and check!='L'):
                print 'left'
                check='L'
                #self.q.put([self.id,Co_MOUSE_LEFT,100])
            pop=points[gesture]
            last=len(points)

        if event.type == MOUSEMOTION:
            points.append( (event.pos[0], event.pos[1]) )

        else:
            points=[]
            last=0

    if last>0:
        point_stop = points[last-1]
    else:
        point_stop=[0,0]

    if last>0:
        if(point_stop==points[last-1]):
            check='S'
            key='S'

    pygame.display.update()
    mainClock.tick(FPS)
'''    
    if __name__  == '__main__':
        qa=Queue()
        Click=DetectMouseClick(q=qa)
        Click.run()
'''
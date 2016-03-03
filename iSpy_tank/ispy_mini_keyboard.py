import pygame
import socket

pygame.init()
pygame.display.set_mode()

TCP_IP = '10.10.1.1'
TCP_PORT = 8150

forward='1121'
backward='1222'
left='1021'
right='1120'
stop='1020'

command=stop

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Test window')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            	print "right"
                command=right
            if event.key == pygame.K_LEFT:
                command=left
                print "left"
            if event.key == pygame.K_UP:
            	command=forward
            	print "up"
            if event.key == pygame.K_DOWN:
                command=backward
                print "down"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
    	s.send(command)
    	s.close()

        if event.type == pygame.KEYUP:
        	command=stop
        	print "stop"
        	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    		s.connect((TCP_IP, TCP_PORT))
    		s.send(command)
    		s.close()
    
    pygame.display.update()
    mainClock.tick(10)	
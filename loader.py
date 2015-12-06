#!/usr/bin/env python
#-*-coding:utf-8 --
#author snccn
#this is the loader of this application
import pygame
from pygame.locals import *
import os
import trafficlights
import sys

#some golbal list
threads=[]
cars=[]
def mainloop():
	global threads
	background_image_filename = 'background.png'
	run=True
	FPS=30
	pygame.init()
	FPSCLOCK=pygame.time.Clock()
	screen=pygame.display.set_mode((800,600),0,32)
	pygame.display.set_caption("Traffic Sim")
	background=pygame.image.load(background_image_filename).convert()
	threads.append(trafficlights.timeloop())
	threads.append(trafficlights.changelight())
	for i in range(0,2):
		threads[i].start()
	while run:
		for event in pygame.event.get():
			if event.type == QUIT:
				run=False
				threads[0].stop()
				threads[1].stop()				
		screen.blit(background,(-90,70))
		trafficlights.changec(screen)
		pygame.display.update()
		FPSCLOCK.tick(FPS)
if __name__=="__main__":
	mainloop()
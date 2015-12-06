#!/usr/bin/env python
#-*-coding:utf-8 --
#author snccn
#this is the loader of this application
import pygame
from pygame.locals import *
import os
import trafficlights
import sys
import cars
#some golbal list
threads=[]
carsb=[]
def draw_status(font,screen):
	global threads
	textsurface=font.render(str(threads[0].isAlive())+str(threads[0].isAlive()),True,(0,0,255))
	textsurface2=font.render(str(trafficlights.basic_time),True,(255,0,0))
	screen.blit(textsurface,(50,50))
	screen.blit(textsurface2,(50,80))
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
	#font = pygame.font.SysFont("arial", 16)
	font = pygame.font.SysFont("arial", 20)
	threads.append(trafficlights.timeloop())
	threads.append(trafficlights.changelight())
	#for i in range(0,1):
	#	threads[i].start()
	threads[0].start()
	threads[1].start()
	#screen2=pygame.display
	ca=cars.carsrunA((244,177,131),(50,375),1,(100,100))
	cb=cars.carsrunB((112,48,160),(180,190),1,(100,100))
	cc=cars.carsrunC((255,255,255),(570,190),1,(100,100))
	while run:
		for event in pygame.event.get():
			if event.type == QUIT:
				run=False
				threads[0].stop()
				threads[1].stop()
		#draw_status(font,screen)
		#these are debug screens
		screen.fill((244,177,131))
		textsurface=font.render(str(threads[0].isAlive())+str(threads[1].isAlive()),True,(0,0,255))
		textsurface2=font.render(str(trafficlights.basic_time),True,(255,0,0))
		textsurface3=font.render("car1: "+str(ca.rect.x)+','+str(ca.rect.y),True,(255,0,0))
		textsurface4=font.render("car2: "+str(cb.rect.x)+','+str(cb.rect.y),True,(0,255,0))
		textsurface5=font.render("car3: "+str(cc.rect.x)+','+str(cc.rect.y),True,(0,0,255))
		textsurface6=font.render("light status: "+str(trafficlights.statusA),True,trafficlights.statusA)
		screen.blit(background,(-90,70))
		screen.blit(textsurface,(0,70))
		screen.blit(textsurface2,(0,90))
		screen.blit(textsurface3,(0,110))
		screen.blit(textsurface4,(0,130))
		screen.blit(textsurface5,(0,150))
		screen.blit(textsurface6,(0,170))
		#end of debug display
		current_time = pygame.time.get_ticks()	
		ca.update(current_time/5,trafficlights.statusA)
		cb.update(current_time/5,trafficlights.statusA)
		cc.update(current_time/5)
		screen.blit(ca.image,ca.rect)
		screen.blit(cb.image,cb.rect)
		screen.blit(cc.image,cc.rect)
		pygame.display.flip()
		trafficlights.changec(screen)
		pygame.display.update()
		FPSCLOCK.tick(FPS)
if __name__=="__main__":
	mainloop()
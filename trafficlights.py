#!/usr/bin/env python
#-*-coding:utf-8 --
#author snccn
#this is the userinterface of traffic sim

#the traffic light defines
import pygame,sys,os,time
from pygame.locals import *
import threading

#there are some global values here
lightcolorA=(255,0,0)
lightcolorB=(17,238,83)
#the main loop time method
statusA,statusB=lightcolorA,lightcolorB
basic_time=0
basic_time_lock=threading.Lock()
class timeloop(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.initrd=0.5 #debug options time initrd
		self.stopth=False
		self.temp=0
	def run(self):
		global basic_time
		while not self.stopth:
			if basic_time_lock.acquire():
				if basic_time_lock.locked():
					basic_time += 1
					basic_time_lock.release()
					print basic_time #debug options debug the main time loop
					time.sleep(self.initrd)
	def stop(self):
		self.stopth=True
class changelight(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.stopflag=False
		self.initrd=0.5
	def run(self):
		global basic_time,statusA,statusB,lightcolorA,lightcolorB
		while not self.stopflag:
			if basic_time_lock.acquire():
				#self.lightchange()
				if basic_time_lock.locked():
					if basic_time % 60 < 31:
						statusA=lightcolorA
						statusB=lightcolorB
					else:
						statusA=lightcolorB
						statusB=lightcolorA
						#pygame.display.flip()
						#self.changec()
					basic_time_lock.release()
				time.sleep(self.initrd)
	def stop(self):
		self.stopflag=True
def changec(screen):
	global lightcolorA,lightcolorB,statusA,statusB
	pygame.draw.circle(screen,statusA,(151,349),5,0)#a
	pygame.draw.circle(screen,statusB,(214,300),5,0)#b
	pygame.draw.circle(screen,statusB,(214,400),5,0)#b
	pygame.draw.circle(screen,statusA,(280,350),5,0)#a
	pygame.draw.circle(screen,statusA,(530,349),5,0)#a
	pygame.draw.circle(screen,statusB,(595,300),5,0)#b
	pygame.draw.circle(screen,statusB,(595,400),5,0)#b
	pygame.draw.circle(screen,statusA,(660,350),5,0)#a
	

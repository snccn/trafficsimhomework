#!/usr/bin/env python
#-*-coding:utf-8 -*-
#cars defines here each thread will return a screen 
import pygame
import pygame.locals
import threading
import time
import trafficlights
cars_pool=[]
cars_pool_lock=threading.Lock()
class cars(pygame.sprite.Sprite):
	def __init__(self,color,position,goal):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([10,10])
		self.rect=self.image.fill(color)
		self.rect.topleft=position
		self.pos=position
		self.goal=goal
		self.flag=(0,0)
class carsrunA(cars):
	def __init__(self,color,inital_position,speed,goal):
		super(carsrunA,self).__init__(color,inital_position,goal)
		self.speed=speed
		self.update_time = 0
	def update(self,basic_time,status):
		if self.update_time < basic_time:
			if status==(255,0,0) and self.rect.x==140 and self.rect.y==375 :
				self.rect.x, self.rect.y = self.rect.x , self.rect.y
			elif self.rect.x <180:
				self.rect.x, self.rect.y = self.rect.x + self.speed, self.rect.y
			if self.rect.x==180:
				self.rect.x,self.rect.y = self.rect.x,self.rect.y + self.speed
			if self.rect.y == 520:
				self.rect.x,self.rect.y = self.rect.x+self.speed,self.rect.y 
			if self.rect.x == 250:
				self.rect.x, self.rect.y = self.rect.x , self.rect.y- self.speed				
			self.update_time = basic_time + 10

class carsrunB(cars):
	def __init__(self,color,inital_position,speed,goal):
		super(carsrunB,self).__init__(color,inital_position,goal)
		self.speed=speed
		self.update_time = 0
	def update(self,basic_time,status):
		if self.update_time < basic_time:
			if status==(255,0,0) and self.rect.x==145 :
				self.rect.x, self.rect.y = self.rect.x , self.rect.y
			elif self.rect.y < 325:
				self.rect.x, self.rect.y = self.rect.x , self.rect.y+ self.speed
			if self.rect.y ==325:
				self.rect.x, self.rect.y = self.rect.x - self.speed, self.rect.y
			if self.rect.x == 50:
				self.rect.x, self.rect.y = self.rect.x , self.rect.y+ self.speed
			if self.rect.y ==375:
				self.rect.x, self.rect.y = self.rect.x+ self.speed , self.rect.y
			if self.rect.x==750 & self.rect.y==375:
				self.rect.x, self.rect.y = 0 , 0
			self.update_time=basic_time+10
			
class carsrunC(cars):
	def __init__(self,color,inital_position,speed,goal):
		super(carsrunC,self).__init__(color,inital_position,goal)
		self.speed=speed
		self.update_time = 0
	def update(self,basic_time):
		if self.update_time<basic_time:
			if self.rect.x ==750 & self.rect.y ==375:
				self.rect.x, self.rect.y = self.rect.x , self.rect.y
			if self.rect.y < 325:
				self.rect.x, self.rect.y = self.rect.x , self.rect.y+ self.speed
			if self.rect.y ==325:
				self.rect.x,self.rect.y = self.rect.x - self.speed,self.rect.y
			#if self.rect.x == 50:
			#	self.rect.x, self.rect.y = self.rect.x , self.rect.y+ self.speed
			#if self.rect.y ==375:
			#	self.rect.x, self.rect.y = self.rect.x + self.speed, self.rect.y
			#if self.rect.x ==750 :
			#	self.rect.x, self.rect.y = self.rect.x , self.rect.y+ self.speed
			#if self.rect.
		
				#continue
			self.update_time=basic_time+10	
		
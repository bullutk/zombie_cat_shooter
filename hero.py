import pygame
from pygame.sprite import Sprite
from settings import Settings

# make the hero a sprite, sprite's 
# are special objects in pygame
# so we need to include the class
class Hero(Sprite):
	# classes have two parts, one is property/data
	# the other are methods
	def __init__(self, screen):
		# because this is a subclass, we need to call super
		# so the parent class gets the data
		super(Hero,self).__init__()
		self.image = pygame.image.load('images/bark_left.png')
		# Rect stuff
		# rect is available on all pygame entities
		self.rect = self.image.get_rect()
		# add the screen to thte object so we can 
		# use and reuse it as needed
		self.screen = screen
		# find out the location and size of our screen
		self.screen_rect = self.screen.get_rect()
		self.rect.centery = self.screen_rect.centery
		self.rect.centerx = self.screen_rect.centerx
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.speed = 1
		# self.speed = settings.hero_speed

	def update_me(self):
		# if user is pushing, move my self.rect left and so on
		if self.moving_right:
			self.rect.centerx += 10 
			self.image = pygame.image.load('images/bark_right.png')
		elif self.moving_left:
			self.rect.centerx -= 10 
			self.image = pygame.image.load('images/bark_left.png')
		if self.moving_down:
			self.rect.centery += 10 
		elif self.moving_up:
			self.rect.centery -= 10 
# 
	# draw method
	def draw_me(self):
		# first argument is what, second is where
		self.screen.blit(self.image, self.rect)

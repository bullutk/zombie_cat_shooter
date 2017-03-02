import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings, direction, bullet_type):
		super(Bullet,self).__init__()
		self.screen = screen
		if bullet_type == 'vert':
			self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
		# elif bullet_type == 'horz':
			# self.rect = pygame.Rect(0,0,game_settings.bullet_height,game_settings.bullet_width)
		self.rect.centerx = hero.rect.centerx
		self.rect.center = hero.rect.center
		self.color = game_settings.bullet_color
		self.speed = game_settings.bullet_speed
		self.x = self.rect.x
		self.y = self.rect.y
		if hero.facing == 'left':
			self.direction = 'left'
		if hero.facing == 'right':
			self.direction = 'right'

	def update(self, hero):
		# change the x and the y accord6ingly 
		# based on self.speed
		# change y in the negative every time it runs
		if self.direction == 'left':
			self.x -= self.speed
		if self.direction == 'right':
			self.x += self.speed

		self.rect.y = self.y
		self.rect.x = self.x

	def draw_bullet(self):
		# draw rect takes three arguments
		# what entity, what color, what 
		pygame.draw.rect(self.screen, self.color, self.rect)


import pygame
import math
from pygame.sprite import Sprite
from settings import Settings

class Enemy(Sprite):
	def __init__(self, image, screen, game_settings):
		super(Enemy, self).__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image,(70,85))
		self.speed = 2
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.screen = screen
		self.rect.centery = self.screen_rect.centery
		self.rect.right = self.screen_rect.right

	def update_me(self, hero):
		dx = self.rect.x - hero.rect.x
		dy = self.rect.y - hero.rect.y
		dist = math.hypot(dx,dy)
		dx = dx / dist
		dy = dy / dist
# hero rect.x is less than enemy rect.x 
		self.rect.x -= dx * self.speed
		self.rect.y -= dy * self.speed

		if self.rect.x < hero.rect.x:
			self.image = pygame.image.load('images/long_cat_right.png')
		else:
			self.image = pygame.image.load('images/long_cat_left.png')

	def draw_me(self):
		self.screen.blit(self.image, self.rect)

import pygame

class Settings():
	def __init__(self):
		display_info = pygame.display.Info()
		self.screen_size = display_info.current_w, display_info.current_h
		self.bg_color = (82,111,53)
		self.bullet_width = 10
		self.bullet_height = 3
		self.bullet_color = (255,255,120)
		self.bullet_speed = 5
		self.timer = 0
		self.game_active = False
		self.enemy_count = 0


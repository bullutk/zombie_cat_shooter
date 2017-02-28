import pygame
import time
import os
from hero import Hero
from settings import Settings
from enemy import Enemy
from pygame.sprite import Group, groupcollide
from game_functions import check_events, update_screen


# core game functionality
def run_game():
	pygame.init()
	# create a settings object
	game_settings = Settings()
	# bg_color = (game_settings.bg_color)
	screen = pygame.display.set_mode(game_settings.screen_size)
	pygame.display.set_caption("Pygame Shooter")
	# create a hero object from our hero class
	the_hero = Hero(screen)
	# make the main game loop... it will run forever
	# the_enemy = Enemy('images/cat.png', screen, game_settings)
	bullets = Group()
	enemies = Group()
	game_start_time = time.time()
	tick = 0

	while 1:
		tick += 1
		screen.fill(game_settings.bg_color)
		game_settings.timer = (time.time() - game_start_time)
		if tick % 100 == 0:
			game_settings.enemy_count += 1
			# print game_settings.enemy_count
			if game_settings.enemy_count == 1:
				game_settings.enemy_count = 0
				enemies.add(Enemy('images/long_cat_left.png', screen, game_settings))

		check_events(screen, the_hero, game_settings, bullets, enemies)
		update_screen(screen, the_hero, game_settings, bullets, enemies)

# run the game
run_game()
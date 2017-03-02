import pygame
import time
import os
from hero import Hero
from settings import Settings
from enemy import Enemy
from pygame.sprite import Group, groupcollide
from game_functions import check_events, update_screen
from background import Background

# core game functionality
def run_game():
	pygame.init()
	# create a settings object
	game_settings = Settings()
	screen = pygame.display.set_mode(game_settings.screen_size)
	pygame.display.set_caption("Zombie Cats IN SPACE")
	background = Background(game_settings)
	# create a hero object from our hero class
	the_hero = Hero(screen)
	# make the main game loop... it will run forever
	# the_enemy = Enemy('images/cat.png', screen, game_settings, 3)
	bullets = Group()
	enemies = Group()
	game_start_time = time.time()
	tick = 0

	while 1:
		tick += 1
		# screen.fill(background)
		game_settings.timer = (time.time() - game_start_time)
		if tick % 100 == 0:
			game_settings.enemy_count += 1
			# print game_settings.enemy_count
			if game_settings.enemy_count == 1:
				game_settings.enemy_count = 0
				enemies.add(Enemy('images/long_cat_left.png', screen, game_settings, 3))

		enemy_hit = groupcollide(enemies, bullets, True, True)
		# for enemy in enemies:
		# 	# print enemies
		# 	enemy.hit(1)
		# 	if enemy.health <= 0:
		# 		enemy.remove(enemies)
		# if enemy_hit:
		# 	os.system("say --r=400 'meow' &")
		check_events(screen, the_hero, game_settings, bullets, enemies)
		update_screen(screen, the_hero, game_settings, bullets, enemies, background)

# run the game
run_game()
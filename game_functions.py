import pygame
import sys
from bullet import Bullet
from enemy import Enemy
from pygame.sprite import Group, groupcollide
import os

def check_events(screen, hero, game_settings, bullets, enemies):
	# want to patch into certain events...
	# like click, keypress, quit, etc...
	for event in pygame.event.get():
		# check to see if the event 
		# that occurs is the quit event
		if event.type == pygame.QUIT:
			sys.exit()
			# the user presses a key
		elif event.type == pygame.KEYDOWN:
			# what key was pressed?
			if event.key == pygame.K_a:
				new_bullet = Bullet(screen,hero,game_settings, 'left', 'vert')
				bullets.add(new_bullet)
				os.system("say --r=750 'bbbbooork' &")
			elif event.key == pygame.K_x:
				new_bullet = Bullet(screen,hero,game_settings, 'down', 'horz')
				bullets.add(new_bullet)
				os.system("say --r=750 'bbbbooork' &")
		# check for keypress
			elif event.key == pygame.K_RIGHT:
				hero.moving_right = True
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True
			elif event.key == pygame.K_UP:
				hero.moving_up = True
			elif event.key == pygame.K_DOWN:
				hero.moving_down = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = False
			elif event.key == pygame.K_LEFT:
				hero.moving_left = False
			elif event.key == pygame.K_UP:
				hero.moving_up = False
			elif event.key == pygame.K_DOWN:
				hero.moving_down = False

def update_screen(screen, the_hero, game_settings, bullets, enemies):
	the_hero.update_me()
	the_hero.draw_me()
	# loop thru all bullets in bullet group
	# call the one we are on bullet
	hero_died = groupcollide(enemies, bullets, True, True)
	if hero_died:
		os.system("say --r=400 'meow' &")

	for bullet in bullets.sprites():
		bullet.update()
		bullet.draw_bullet()
	for enemy in enemies:
		enemy.update_me(the_hero)
		enemy.draw_me()
	# flip the screen, i.e., wipe it 
	# out so pygaem can redraw
	pygame.display.flip()

	# print enemies





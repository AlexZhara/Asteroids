# asteroids/game.py

import pygame
from utils import load_sprite, get_random_position, load_sound
from models import Spaceship, Asteroid

class Asteroids:

	MIN_ASTEROID_DISTANCE = 250
	
	def __init__(self):
		# Initialise pygame and set the game's title
		pygame.init()
		pygame.display.set_caption("Asteroids")

		# Initialise main screen & game clock
		self.screen = pygame.display.set_mode((800, 600))
		self.background = load_sprite("space", "jpeg", False) # args: filename, file extension, is it transparent
		self.clock = pygame.time.Clock()

		# Initialise game objects
		self.asteroids = []
		self.bullets = []
		self.spaceship = Spaceship((400, 300), self.bullets.append)

		# Initialise sounds
		self.rock_smash = load_sound("rock_smash")
		self.rock_smash.set_volume(0.35)

		self.music = load_sound("Level 3")
		self.music.set_volume(0.3)
		self.music.play()
		

		for _ in range(6):
			while True:
				position = get_random_position(self.screen)
				if position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE:
					break

			self.asteroids.append(Asteroid(position, self.asteroids.append))


	def main_loop(self):
		while True:
			self._handle_input()
			self._game_logic()
			self._draw()

	def _get_game_objects(self):
		game_objects = [*self.asteroids, *self.bullets]

		if self.spaceship:
			game_objects.append(self.spaceship)

		return game_objects

	def _handle_input(self):
		# Event loop. Handles one time key presses
		for event in pygame.event.get():
			if event.type == pygame.QUIT or \
			(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				quit()
			elif \
			(self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
				self.spaceship.shoot()

		is_key_pressed = pygame.key.get_pressed()

		if self.spaceship:
			if is_key_pressed[pygame.K_RIGHT]:
				self.spaceship.rotate(clockwise=True)
			elif is_key_pressed[pygame.K_LEFT]:
				self.spaceship.rotate(clockwise=False)
			elif is_key_pressed[pygame.K_UP]:
				self.spaceship.accelerate()
			elif is_key_pressed[pygame.K_DOWN]:
				self.spaceship.brake()

	def _game_logic(self):
		#self.spaceship.move(self.screen)
		for game_object in self._get_game_objects():
			game_object.move(self.screen)

		if self.spaceship:
			for asteroid in self.asteroids:
				if asteroid.collides_with(self.spaceship):
					self.spaceship = None
					break

		for bullet in self.bullets[:]:
			for asteroid in self.asteroids[:]:
				if asteroid.collides_with(bullet):
					self.asteroids.remove(asteroid)
					self.bullets.remove(bullet)
					asteroid.split()
					print(self.rock_smash.get_volume())
					self.rock_smash.play()
					break

		for bullet in self.bullets[:]: # Creating a copy of bullets list, because removing elements from list while iterating can cause issues
			if not self.screen.get_rect().collidepoint(bullet.position): # All surfaces have get_rect() method that returns rectangular area.
				self.bullets.remove(bullet)								 # And each rectangle has a collidepoint() method that checks for collision.

	def _draw(self):
		self.screen.blit(self.background, (0, 0))

		#self.spaceship.draw(self.screen)
		for game_object in self._get_game_objects():
			game_object.draw(self.screen)

		pygame.display.flip()
		self.clock.tick(60)












# asteroids/game.py

import pygame
from utils import load_sprite, get_random_position
from models import Spaceship, Asteroid

class Asteroids:

	MIN_ASTEROID_DISTANCE = 250
	
	def __init__(self):
		# Initialise pygame and set the game's title
		pygame.init()
		pygame.display.set_caption("Asteroids")

		self.screen = pygame.display.set_mode((800, 600))
		self.background = load_sprite("space", "jpeg", False) # args: filename, file extension, is it transparent
		self.clock = pygame.time.Clock()

		self.spaceship = Spaceship((400, 300))
		self.asteroids = []

		for _ in range(6):
			while True:
				position = get_random_position(self.screen)
				if position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE:
					break

			self.asteroids.append(Asteroid(position))


	def main_loop(self):
		while True:
			self._handle_input()
			self._game_logic()
			self._draw()

	def _get_game_objects(self):
		game_objects = [*self.asteroids]
		if self.spaceship:
			game_objects.append(self.spaceship)

		return game_objects

	def _handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT or \
			(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				quit()

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

	def _draw(self):
		self.screen.blit(self.background, (0, 0))

		#self.spaceship.draw(self.screen)
		for game_object in self._get_game_objects():
			game_object.draw(self.screen)

		pygame.display.flip()
		self.clock.tick(60)












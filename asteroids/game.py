# asteroids/game.py

import pygame
from utils import load_sprite
from models import GameObject

class Asteroids:
	
	def __init__(self):
		# Initialise pygame and set the game's title
		pygame.init()
		pygame.display.set_caption("Asteroids")

		self.screen = pygame.display.set_mode((800, 600))
		self.background = load_sprite("space", "jpeg", False) # args: filename, file extension, is it transparent

		self.spaceship = GameObject((400, 300), load_sprite("spaceship_small", "png"), (0, 0))
		self.asteroid = GameObject((400, 300), load_sprite("asteroid", "png"), (1, 0))

	def main_loop(self):
		while True:
			self._handle_input()
			self._game_logic()
			self._draw()

	def _handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT or \
			(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				quit()

	def _game_logic(self):
		self.spaceship.move()
		self.asteroid.move()

	def _draw(self):
		self.screen.blit(self.background, (0, 0))
		self.spaceship.draw(self.screen)
		self.asteroid.draw(self.screen)
		pygame.display.flip()
"""This is the module where the main game class is defined."""

import pygame
from utils import load_sprite, get_random_position, load_sound, print_msg
from models import Spaceship, Asteroid

class Asteroids:
	"""Main game class that initialises all the needed variables and sets up the main game loop."""
	MIN_ASTEROID_DISTANCE = 250 # How big is the area in the centre (around the ship) where asteroids cannot spawn?
	NUM_OF_ASTEROIDS = 6 		# How many asteroids when game starts?
	
	def __init__(self):
		"""Initialises everything needed for pygame to work."""
		# Initialise pygame and set the game's title
		pygame.init()
		pygame.display.set_caption("Asteroids")

		# Initialise main screen, game clock and (empty) game over message
		self.screen = pygame.display.set_mode((800, 600))
		self.background = load_sprite("space", "jpeg", False) # args: filename, file extension, is it transparent
		self.clock = pygame.time.Clock()
		self.font = pygame.font.Font(None, 64) # Args: font file (None is default), size in pixels
		self.message = ""

		# Initialise game objects
		self.asteroids = []
		self.bullets = []
		self.spaceship = Spaceship((400, 300), self.bullets.append) # Args: spawning location; callback function for shooting bullets

		# Spawning asteroids, taking into account safe space in the middle
		for _ in range(NUM_OF_ASTEROIDS):
			while True:
				position = get_random_position(self.screen)
				if position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE:
					break

			self.asteroids.append(Asteroid(position, self.asteroids.append))

		# Initialise sounds
		self.rock_smash = load_sound("rock_smash")
		self.rock_smash.set_volume(0.35)
		self.explosion = load_sound("explosion")
		self.explosion.set_volume(0.5)
		self.music = load_sound("Level 3")
		self.music.set_volume(0.3)
		self.music.play()
		

	def main_loop(self):
		"""In every iteration check for user input, handle game logic and render the frame."""
		while True:
			self._handle_input()
			self._game_logic()
			self._draw()

	def _get_game_objects(self):
		"""Return all currently present game objects."""
		game_objects = [*self.asteroids, *self.bullets]

		if self.spaceship:
			game_objects.append(self.spaceship)

		return game_objects

	def _handle_input(self):
		"""Handle user inputs, both single key presses and constantly held keys."""
		# Event loop. Handles one time key presses
		for event in pygame.event.get():
			if event.type == pygame.QUIT or \
			(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				quit()
			elif \
			(self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
				self.spaceship.shoot()

		# Handles constant key presses, ie holding Up-Down-Left-Right arrow keys
		is_key_pressed = pygame.key.get_pressed()
		if self.spaceship: # If the ship is still alive...
			if is_key_pressed[pygame.K_RIGHT]:
				self.spaceship.rotate(clockwise=True)
			elif is_key_pressed[pygame.K_LEFT]:
				self.spaceship.rotate(clockwise=False)
			elif is_key_pressed[pygame.K_UP]:
				self.spaceship.accelerate()
			elif is_key_pressed[pygame.K_DOWN]:
				self.spaceship.decelerate()

	def _game_logic(self):
		"""Handles primary game logic."""
		# Handles game object movement.
		for game_object in self._get_game_objects():
			game_object.move(self.screen)

		# Handles victory logic
		if not self.asteroids and self.spaceship:
			self.message = "You won!"

		# Handles game over logic.
		if self.spaceship:
			for asteroid in self.asteroids:
				if asteroid.collides_with(self.spaceship):
					self.explosion.play()
					self.spaceship = None
					self.message = "You lost!"
					break

		# Handles shooting asteroids
		for bullet in self.bullets[:]:
			for asteroid in self.asteroids[:]:
				if asteroid.collides_with(bullet):
					self.asteroids.remove(asteroid)
					self.bullets.remove(bullet)
					asteroid.split()
					self.rock_smash.play()
					break

		# Handles bullets disappearing when reaching screen edge
		for bullet in self.bullets[:]: # Creating a copy of bullets list, because removing elements from list while iterating can cause issues
			if not self.screen.get_rect().collidepoint(bullet.position): # All surfaces have get_rect() method that returns rectangular area.
				self.bullets.remove(bullet)								 # And each rectangle has a collidepoint() method that checks for collision.



	def _draw(self):
		"""Handles screen rendering."""
		self.screen.blit(self.background, (0, 0)) # Projects the background image

		# Draws each game object onto the screen
		for game_object in self._get_game_objects():
			game_object.draw(self.screen)

		# Prints the win/loss message
		if self.message:
			print_msg(self.screen, self.message, self.font)

		# The flip() method updates the entire game screen at once.
		pygame.display.flip()

		# Locking 60 FPS
		self.clock.tick(60)












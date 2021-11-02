"""This is a Hello, world! type program that spawns colourful circles all over the game screen.

This file has nothing to do with the Asteroids game, but I included it in the repo for posterity's sake.
"""
import pygame
import random

pygame.init() 								 # Starts up the game engine
pygame.display.set_caption('Hello, Shapes!') # Sets the game title
screen = pygame.display.set_mode((800, 600)) # screen variable holds the main pygame surface. Tuple argument = screen dimensions

def generate_colour():
	"""Generates a random RGB colour."""
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r,g,b)

# This is where the main game loop starts.
# In every iteration it checks for events, processes game logic, and renders the frame.

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	screen.fill((135, 206, 235))			# Fills the game screen with a shade of blue (RGB values in the tuple)
	x = random.randint(10, 790)				# Generating values for our circles
	y = random.randint(10, 790)
	r = random.randint(2, 50)
	pygame.draw.circle(screen, generate_colour(), (x, y), r) # Arguments: (surface, colour, coords, radius)
	pygame.display.flip()					# Actually renders the frame from the buffer onto the screen.
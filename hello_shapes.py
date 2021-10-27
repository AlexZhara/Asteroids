# Spawning circles all over the place!

import pygame
import random

pygame.init() 								 # Starts up the game engine
pygame.display.set_caption('Hello, Shapes!') # Sets the game title
screen = pygame.display.set_mode((800, 600)) # screen variable holds the pygame surface. Tuple argument = screen dimensions

def generate_colour():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r,g,b)

# This is where the main game loop starts.
# In every iteration it checks for events, or user inputs.
# If you press the close game, the game quits.

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
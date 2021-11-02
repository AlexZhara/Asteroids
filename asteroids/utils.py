"""This module defines some helper functions used in other modules."""

from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame import Color
from pathlib import Path
import random

def load_sprite(name, file_type, with_alpha=True):
	"""Load the sprite.

	Args:
		name (str) - the file's name
		file_type (str) - the file's type (eg 'png' or 'jpeg')
		with_alpha (bool) - alpha transparency enabled?
	"""
	filepath = Path(__file__).parent / Path("assets/sprites/" + name + ".{}".format(file_type))
	
	sprite = load(filepath.resolve())

	if with_alpha:
		return sprite.convert_alpha() # You *could* just return convert_alpha(), but it's more resource intensive than convert()

	return sprite.convert()

def load_sound(name):
	"""Load the sound by its name."""
	filepath = Path(__file__).parent / Path("assets/sounds/" + name + ".wav")
	return Sound(filepath.resolve())

def print_msg(surface, text, font, color=Color("tomato")): # Args: target surface for render, the text, the font, the color
	"""Print the given message.

	Args:
		surface (Surface object) - surface onto which the msg prints
		text (str) - the text to print
		font (Font object) - pygame's font object, the text's font
		color (Color object) - pygame's color object, the text's colour
	"""
	text_surface = font.render(text, True, color) # Args: the text, antialiasing flag, color

	rect = text_surface.get_rect()
	rect.center = Vector2(surface.get_size()) / 2

	surface.blit(text_surface, rect)


def wrap_position(position, surface):
	"""Wrap around the game screen when moving past its edge."""
	x, y = position
	w, h = surface.get_size()
	return Vector2(x % w, y % h)

def get_random_position(surface):
	"""Return random position as a vector."""
	return Vector2(
		random.randrange(surface.get_width()),
		random.randrange(surface.get_height())
		)

def get_random_velocity(min_speed, max_speed):
	"""Return random velocity as a vector."""
	speed = random.randint(min_speed, max_speed)
	angle = random.randrange(0, 360)
	return Vector2(speed, 0).rotate(angle)
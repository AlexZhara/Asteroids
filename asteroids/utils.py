# asteroids/utils.py
# Reusable utility (helper) methods

from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame import Color
from pathlib import Path
import random

def load_sprite(name, file_type, with_alpha=True):
	filepath = Path(__file__).parent / Path("assets/sprites/" + name + ".{}".format(file_type))
	
	sprite = load(filepath.resolve())

	if with_alpha:
		return sprite.convert_alpha() # You *could* just return convert_alpha(), but it's more resource intensive than convert()

	return sprite.convert()

def load_sound(name):
	filepath = Path(__file__).parent / Path("assets/sounds/" + name + ".wav")
	return Sound(filepath.resolve())

def print_msg(surface, text, font, color=Color("tomato")): # Args: target surface for render, the text, the font, the color
	text_surface = font.render(text, True, color) # Args: the text, antialiasing flag, color

	rect = text_surface.get_rect()
	rect.center = Vector2(surface.get_size()) / 2

	surface.blit(text_surface, rect)


def wrap_position(position, surface):
	x, y = position
	w, h = surface.get_size()
	return Vector2(x % w, y % h)

def get_random_position(surface):
	return Vector2(
		random.randrange(surface.get_width()),
		random.randrange(surface.get_height())
		)

def get_random_velocity(min_speed, max_speed):
	speed = random.randint(min_speed, max_speed)
	angle = random.randrange(0, 360)
	return Vector2(speed, 0).rotate(angle)
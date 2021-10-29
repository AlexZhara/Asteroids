# asteroids/utils.py
# Reusable utility (helper) methods

from pygame.image import load
from pygame.math import Vector2
from pathlib import Path
import random

def load_sprite(name, file_type, with_alpha=True):
	filepath = Path(__file__).parent / Path("assets/sprites/" + name + ".{}".format(file_type))
	
	sprite = load(filepath.resolve())

	if with_alpha:
		return sprite.convert_alpha() # You *could* just return convert_alpha(), but it's more resource intensive than convert()

	return sprite.convert()

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
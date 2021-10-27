# asteroids/utils.py
# Helper methods

from pygame.image import load
from pathlib import Path

def load_sprite(name, file_type, with_alpha=True):
	filename = Path(__file__).parent / Path("assets/sprites/" + name + ".{}".format(file_type))
	print("The filename is {}".format(filename))
	sprite = load(filename.resolve())

	if with_alpha:
		return sprite.convert_alpha()

	return sprite.convert()
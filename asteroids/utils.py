# asteroids/utils.py
# Reusable utility (helper) methods

from pygame.image import load
from pathlib import Path

def load_sprite(name, file_type, with_alpha=True):
	filepath = Path(__file__).parent / Path("assets/sprites/" + name + ".{}".format(file_type))
	
	sprite = load(filepath.resolve())

	if with_alpha:
		return sprite.convert_alpha() # You *could* just return convert_alpha(), but it's more resource intensive than convert()

	return sprite.convert()

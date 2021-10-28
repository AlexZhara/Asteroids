# asteroids/models.py
# This is where game objects live

from pygame.math import Vector2
from pygame.transform import scale

class GameObject:
	def __init__(self, position, sprite, velocity): # args: position = centre of object; velocity = updates the position each frame
		self.position = Vector2(position)
		self.sprite = sprite
		self.radius = sprite.get_width() / 2 # could also use height since dealing with square sprites only
		self.velocity = Vector2(velocity)

	def draw(self, surface):
		"""Draws the object's sprite onto the surface passed as the argument
		"""
		blit_position = self.position - Vector2(self.radius) # Subtracting vector to get top-left corner start
		surface.blit(self.sprite, blit_position)

	def move(self):
		"""Moves object by updating position based on velocity
		"""
		self.position = self.position + self.velocity

	def collides_with(self, other):
		"""Collision checker. Returns true if the distance < the sum of radiuses
		"""
		distance = self.position.distance_to(other.position) # Vector2.distance_to()
		return distance < self.radius + other.radius
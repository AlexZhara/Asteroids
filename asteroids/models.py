# asteroids/models.py
# This is where game objects live

from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite, wrap_position, get_random_velocity

UP = Vector2(0, -1)

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

	def move(self, surface):
		"""Moves object by updating position based on velocity
		"""
		self.position = wrap_position(self.position + self.velocity, surface)

	def collides_with(self, other):
		"""Collision checker. Returns true if the distance < the sum of radiuses
		"""
		distance = self.position.distance_to(other.position) # Vector2.distance_to()
		return distance < self.radius + other.radius

class Spaceship(GameObject):

	ROTATION_SPEED = 2  # Angle (in degrees) by which ship rotates each frame
	ACCELERATION = 0.15
	BULLET_SPEED = 3

	def __init__(self, position, create_bullet_callback):
		super().__init__(position, load_sprite("spaceship_small", "png"), Vector2(0))
		self.direction = Vector2(UP) # Making a copy of UP to modify later
		self.create_bullet_callback = create_bullet_callback

	def rotate(self, clockwise=True):
		"""Changes the direction by rotating it clockwise or anticlockwise
		"""
		sign = 1 if clockwise else -1
		angle = self.ROTATION_SPEED * sign
		self.direction.rotate_ip(angle)

	def draw(self, surface):
		"""Draws the spaceship onto the surface passed as argument
		"""
		angle = self.direction.angle_to(UP) # Translates spaceship's direction into rotation angle in degrees
		rotated_surface = rotozoom(self.sprite, angle, 1.0) # Rotates the sprite. Last arg is scale change, hence 1.0
		rotated_surface_size = Vector2(rotated_surface.get_size())
		blit_position = self.position - rotated_surface_size * 0.5 # Blit position calculated based on rotated surface size, which differs from original size
		surface.blit(rotated_surface, blit_position)

	def accelerate(self):
		self.velocity += self.direction * self.ACCELERATION

	def brake(self):
		self.velocity -= self.direction * self.ACCELERATION

	def shoot(self):
		bullet_velocity = self.BULLET_SPEED * self.direction + self.velocity # Always shoots in direction of ship + adjusts for ship velocity
		bullet = Bullet(self.position, bullet_velocity)
		self.create_bullet_callback(bullet)

class Asteroid(GameObject):

	def __init__(self, position):
		super().__init__(position, load_sprite("asteroid", "png"), get_random_velocity(1, 3))


class Bullet(GameObject):

	def __init__(self, position, velocity):
		super().__init__(position, load_sprite("bullet", "png"), velocity)

	def move(self, surface):
		self.position = self.position + self.velocity






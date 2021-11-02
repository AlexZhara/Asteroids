"""This module defines all of the game's objects.

The custom base GameObject class is defined, which is the parent class for other game objects,
of which there are three: Spaceship, Asteroid and Bullet.
"""
from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite, load_sound, wrap_position, get_random_velocity


UP = Vector2(0, -1) 
"""A constant that points towards top of screen."""

class GameObject:
	"""Base class for all game objects."""
	def __init__(self, position, sprite, velocity): # args: position = centre of object; velocity = updates the position each frame
	"""Initialise game object.

	Args:
		position (tuple) - coordinates for the object's centre
		sprite (Surface object) - use load_sprite() helper function
		velocity (tuple) - vector value that represents the object's movement velocity

	"""
		self.position = Vector2(position)
		self.sprite = sprite
		self.radius = sprite.get_width() / 2 # could also use height since dealing with square sprites only
		self.velocity = Vector2(velocity)

	def draw(self, surface):
		"""Draw the object's sprite onto the surface passed as the argument."""
		blit_position = self.position - Vector2(self.radius) # Subtracting vector to get top-left corner start
		surface.blit(self.sprite, blit_position)

	def move(self, surface):
		"""Moves object by updating position based on velocity."""
		self.position = wrap_position(self.position + self.velocity, surface)

	def collides_with(self, other):
		"""Return true if the distance < the sum of radiuses."""
		distance = self.position.distance_to(other.position) # Vector2.distance_to()
		return distance < self.radius + other.radius

class Spaceship(GameObject):
	"""Player controlled spaceship.

	Class variables:
		ROTATION_SPEED (int) - how fast the ship rotates left/right
		ACCELERATION (float) - how fast the ship accelerates/decelerates
		BULLET_SPEED (int) - how fast the bullets go
	"""
	ROTATION_SPEED = 2 
	ACCELERATION = 0.15
	BULLET_SPEED = 3

	def __init__(self, position, create_bullet_callback):
		"""Initialise spaceship.

		Args:
			position (tuple) - coordinates for spawning spaceship
			create_bullet_callback (func) - callback function for adding bullet to bullets list
		"""
		self.direction = Vector2(UP) # Making a copy of UP to modify later
		self.create_bullet_callback = create_bullet_callback
		self.laser_sound = load_sound("laser")
		super().__init__(position, load_sprite("spaceship_small", "png"), Vector2(0))

	def rotate(self, clockwise=True):
		"""Change the direction by rotating it clockwise or anticlockwise."""
		sign = 1 if clockwise else -1
		angle = self.ROTATION_SPEED * sign
		self.direction.rotate_ip(angle)

	def draw(self, surface):
		"""Draw the spaceship onto the surface passed as argument."""
		angle = self.direction.angle_to(UP) # Translates spaceship's direction into rotation angle in degrees
		rotated_surface = rotozoom(self.sprite, angle, 1.0) # Rotates the sprite. Last arg is scale change, hence 1.0
		rotated_surface_size = Vector2(rotated_surface.get_size())
		blit_position = self.position - rotated_surface_size * 0.5 # Blit position calculated based on rotated surface size, which differs from original size
		surface.blit(rotated_surface, blit_position)

	def accelerate(self):
		"""Move the ship forward."""
		self.velocity += self.direction * self.ACCELERATION

	def decelerate(self):
		"""Move the ship backwards."""
		self.velocity -= self.direction * self.ACCELERATION

	def shoot(self):
		"""Shoot a bullet."""
		bullet_velocity = self.BULLET_SPEED * self.direction + self.velocity # Always shoots in direction of ship + adjusts for ship velocity
		bullet = Bullet(self.position, bullet_velocity)
		self.create_bullet_callback(bullet)
		self.laser_sound.play()

class Asteroid(GameObject):
	"""The eponymous asteroids."""
	def __init__(self, position, create_asteroid_callback, size=3):
		"""Initiate asteroid.

		Args:
			position (tuple) - coordinates for spawning the asteroid
			create_asteroid_callback (func) - callback function for adding asteroid to asteroids list
			size (int) - value between 1-3 that defines how large the asteroid is
		"""
		self.size = size
		self.create_asteroid_callback = create_asteroid_callback

		size_to_scale = {
			3: 1,
			2: 0.5,
			1: 0.25
		}
		scale = size_to_scale[size]
		sprite = rotozoom(load_sprite("asteroid", "png"), 0, scale)

		super().__init__(position, sprite, get_random_velocity(1, 3))

	def split(self):
		"""Split asteroid in two if it's not already the smallest size."""
		if self.size > 1:
			for _ in range(2):
				asteroid = Asteroid(self.position, self.create_asteroid_callback, self.size-1)
				self.create_asteroid_callback(asteroid)


class Bullet(GameObject):
	"""Bullet objects."""
	def __init__(self, position, velocity):
		"""Initialise the bullet.

		Args:
			position (tuple) - coordinates for spawning the bullet
			velocity (tuple) - the bullet's velocity
		"""
		super().__init__(position, load_sprite("bullet", "png"), velocity)

	def move(self, surface):
		"""Override the original move method to avoid wrap_around game screen."""
		self.position = self.position + self.velocity






"""This module sets up the Game object and launches the main loop method, thereby launching the game."""
from game import Asteroids

# Checking if the script is run as code vs being run as a module
# Kind of redundant since you likely won't run it as a module,
# but I'm still adding this here, to signify the game's entry point.
if __name__ == '__main__':
	asteroids = Asteroids()
	asteroids.main_loop()
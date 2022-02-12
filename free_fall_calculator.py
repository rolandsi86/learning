from math import sqrt
GRAVITY=9.80665

class FreeFall:
	"""Calculates time of fall and velocity."""

	def __init__(self, height):
		self.height = height

	def velocity(self):
		"""Calculates velocity"""
		velocity = self.time * GRAVITY
		print(f"Velocity is {round(velocity,2)}m/s.")

	def time_of_fall(self):
		"""Calculates free fall time depending on height."""
		result=(2*self.height)/GRAVITY
		self.time=sqrt(result)
		
		#assign new variable output' to split text in 2 lines.
		output=f"Time of fall (t) from {self.height}m altitude takes "
		output+=f"{round(self.time,2)}s to reach the ground."
		print(output)
		
		self.velocity()

test=FreeFall(150)
test.time_of_fall()



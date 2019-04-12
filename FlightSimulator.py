from random import gauss
from time import sleep

class FlightSimulator:

	def __init__(self):
		self.current_angle = 0

	def fly(self):
		while True:
			print("Oh boi, turbulances...")
			sleep(1)
			self.generate_turbulance(0,30)
			print("Current angle: ", self.current_angle)
			sleep(1)
			print("Maidai Maidai we need to correct angle... Tilt correction launched")
			sleep(1)
			self.correct_angle();
			print("Thanks God for this device...")
			print("Current angle (after tilt correction): ", self.current_angle)
			sleep(1)

	def generate_turbulance(self,mu, sigma):
		self.current_angle = gauss(mu, sigma)

	def correct_angle(self):
		if self.current_angle > 0.0:
			print("Turning right ", abs(int(self.current_angle)), " degrees")
		else:
			print("Turning left", abs(int(self.current_angle)), " degrees")

		self.current_angle -= int(self.current_angle)

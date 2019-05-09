#
# Flight simulator.
# Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth).
# The program should print out current orientation, and applied tilt correction.
# The program should run in infinite loop, until user breaks the loop.
# Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations").

# With every simulation step the orentation should be corrected, applied and printed out.
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
#
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# When you are done upload this code to your github repository.
#
# Delete these comments before commit!
# Good luck.


from FlightSimulator import Plane
from FlightSimulator import Environment
from FlightSimulator import scenarios_generator
from time import sleep

if __name__ == "__main__":
    for wind_scenario in scenarios_generator():
        environment = Environment(wind_scenario)
        environment.add_plane(Plane("F2-1", 1))
        environment.add_plane(Plane("F15", 1.5))
        environment.add_plane(Plane("Boeing 777", 0.5))

        for simulation_step in environment:
            sleep(1)
            print(simulation_step)

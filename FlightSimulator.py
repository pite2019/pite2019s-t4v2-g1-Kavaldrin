from random import gauss
from random import randint
import logging

logging.basicConfig(level=logging.INFO)

DAMAGE_ANGLE = 60
CRASH_ANGLE = 90
MAX_DAMAGE = 10
SCENARIO_SIZE = 1000


class Wind:
    NO_WIND = 0
    BREEZE = 1
    GALE = 2
    HURRICANE = 3


class PlaneStatus:
    OK = 0
    DAMAGED = 1
    CRASHED = 2


def scenarios_generator():
    for starting_wind in range(Wind.HURRICANE - Wind.NO_WIND + 1):
        yield starting_wind


class Environment:
    def __init__(self, wind_level):
        self.windLevel = wind_level
        self.planesInSystem = []
        self.windCounter = 0
        self.planesStatus = ''
        self.steps = SCENARIO_SIZE

    def add_plane(self, plane):
        self.planesInSystem.append(plane)

    def check_planes_status(self):

        crashed_planes = []
        for plane in self.planesInSystem:
            if plane.status == PlaneStatus.CRASHED:
                crashed_planes.append(plane)

        for crashedPlane in crashed_planes:
            self.planesInSystem.remove(crashedPlane)

    def affect_on_planes(self):
        for plane in self.planesInSystem:
            plane.generate_turbulence(self.windLevel)
            plane.correct_tilt_angle()
            plane.check_status()
            self.planesStatus += 'Plane {} tilt {}\n'.format(plane.name, plane.tiltAngle)

    def wind_change(self):

        self.windCounter += 1
        if self.windCounter >= 10:
            self.windLevel = randint(Wind.NO_WIND, Wind.HURRICANE)
            self.windCounter = 0

    def __next__(self):

        self.steps -= 1
        self.planesStatus = ''
        if len(self.planesInSystem) > 0 and self.steps > 0:
            self.check_planes_status()
            self.affect_on_planes()
            self.wind_change()
            return self.planesStatus
        else:
            raise StopIteration()

    def __iter__(self):
        return self


class Plane:
    def __init__(self, name, tilt_correction):
        logging.info('Creating plane called {} with tilt correction {}'.format(name, tilt_correction))
        self.tiltAngle = 0
        self.name = name
        self.tiltCorrection = tilt_correction
        self.status = PlaneStatus.OK
        self.damage_counter = 0

    def generate_turbulence(self, wind_level):
        self.tiltAngle += gauss(0.75, 1.0 * wind_level)
        logging.info('Tilt after turbulence {}'.format(self.tiltAngle))

    def correct_tilt_angle(self):
        tilt_correction = min(abs(self.tiltCorrection), abs(self.tiltAngle))
        logging.info('Correction of tilt {} degrees'.format(tilt_correction))

        if self.tiltAngle > 0:
            logging.info('Turning left for {} degrees'.format(tilt_correction))
            self.tiltAngle -= tilt_correction
        else:
            logging.info('Turning right for {} degrees'.format(tilt_correction))
            self.tiltAngle += tilt_correction

    def check_status(self):
        if self.tiltAngle > DAMAGE_ANGLE or self.tiltAngle < -DAMAGE_ANGLE:
            logging.warning('Plane is getting DAMAGE!')
            self.status = PlaneStatus.DAMAGED  # can be overwritten :)
            self.damage_counter += 1
            if self.damage_counter > MAX_DAMAGE:
                logging.critical('Plane has crashed :(')
                self.status = PlaneStatus.CRASHED
                return None  # just to exit function faster

        elif self.tiltAngle > CRASH_ANGLE or self.tiltAngle < -CRASH_ANGLE:
            logging.critical('Plane has crashed :(')  # same line, but to avoid changing logic
            self.status = PlaneStatus.CRASHED

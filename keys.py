import pygame
from pygame.locals import *
import keyboard


class Controls:
    def __init__(self):
        self.right = K_RIGHT
        self.left  = K_LEFT
        ...

    def __call__(self,key):
        return keyboard.is_pressed(key)
        # keys = pygame.key.get_pressed()
        # return keys[self.__dict__[key]]

controls = Controls()
def car_controls(car):
    # asdada
    # car.x += 1
    # if car.y > 180:
        if controls('q'):
            car.xac -= 0.1
        if controls('e'):
            car.xac += 0.1

        car.xac /= 1.001
    # ...


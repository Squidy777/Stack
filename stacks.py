import pymunk as pm
from pymunk import Vec2d,space,Poly
from keys import *
import pygame
import pymunk

import math




class Polygon():
    def __init__(self, pos, length, height, space, mass=0.01):
        moment = 300000
        body = pm.Body(mass, moment)
        body.position = Vec2d(*pos)

        shape = pm.Poly.create_box(body, (length, height))
        shape.friction = 30
        shape.color = (0, 0, 255)
        shape.collision_type = 2
        shape.elasticity = 0

        # shape.
        space.add(body, shape)
        self.body = body
        self.shape = shape
        self._super_colide = False
        wood = pygame.image.load("log.png").convert_alpha()
        # wood2 = pygame.image.load("log.png").convert_alpha()
        rect = pygame.Rect(251, 357, 86, 22)

        self.beam_image = wood.subsurface(rect).copy()

        # rect = pygame.Rect(16, 252, 22, 84)
        # self.column_image = wood2.subsurface(rect).copy()

    def to_pygame(self, p):
        """Convert pymunk to pygame coordinates"""
        return int(p.x), int(-p.y+600)

    def super_colide(self,boolean):
        self._super_colide = boolean



    def draw_poly(self, screen,camera):
        element = 'beams'
        poly = self.shape
        if element == 'beams':
            p = poly.body.position
            p = Vec2d(*self.to_pygame(p))
            angle_degrees = math.degrees(poly.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.beam_image,
                                                       angle_degrees)

            offset = Vec2d(*rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            scale = camera.scale

            rotated_logo_img = pygame.transform.scale(rotated_logo_img,([int(a*scale) for a in rotated_logo_img.get_size()]))
            screen.blit(rotated_logo_img, ((np.x+camera.x)*scale+450, (np.y+camera.y)*scale+600))


class Car(Polygon):
    def __init__(self,pos, length, height, space, mass=5.0):
        super(Car, self).__init__(pos, length, height, space, mass=mass)
        self.controls = Controls()
        self.body.body_type = pymunk.Body.KINEMATIC



    def __call__(self):
        if self.controls('RIGHT'):
            self.shape.body.velocity += (30.43,0)

        if self.controls('LEFT'):
            self.shape.body.velocity += (-30.43,0)



        ...

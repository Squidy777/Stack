from Personal.Pygame import *
from stacks import *
import pymunk
from time import time
from ui import *
from threading import Thread

from playsound import playsound

def play():
    while True:
        playsound('LD49 - Startup (1).wav')

Thread(target=play, args=()).start()
from datetime import timedelta

def vehicle():
    ...


def collides(sprite1,sprite2):
    sprite1_group = pygame.sprite.RenderUpdates()    #this creates a render updates group, as the sprite collide function requires one of its arguments to be a group.
    sprite1_group.add(sprite1)
    collisions = pygame.sprite.spritecollide(sprite2, sprite1_group, False)  #runs spritecollide, specifying the sprite, the group, and the last parameter, which should almost always be false.
    for other in collisions:
        if other != sprite2:     #spritecollide registers a sprites collision with itself, so this filters it
            return True

def ground():
    x = 0
    y = -200

    xln = 1000
    yln = 800

    body = pymunk.Body(body_type=pymunk.Body.STATIC)

    # body.position = (pos_x, pos_y)
    shape = pymunk.Poly.create_box(body, (-200000, -0))
    space.add(body, shape)
    return shape


p = (980, 240)
space = space.Space()
space.gravity =  (0.0, -10.0)


beams = [Car((500,00), 85, 20, space)]
g = ground()

# ground = Polygon((100,-900), 85, 20, space)


# py_game = Pygame()
#
# @py_game
# def init():
#     ...

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.scale = 1
        ...

camera = Camera()
player = beams[0]
highest = [0]
score = 0.1



bg = pygame.image.load("sky.png")
#INSIDE OF THE GAME LOOP

time_ = time()
@Pygame
def per_frame():
    global time_
    global score

    screen.blit(bg, (0, 0))

    if not randint(0,40):
        beams.append(
            Polygon((player.body.position.x + player.body.velocity.x * 5, 900-(camera.scale*20)+600+randint(-200,200)), 85, 20, space)
        )

    dt = 1.0 / 50.0 / 2.
    for x in range(2):
        space.step(1e+8/time_)

    print(1e+8/time_)

    player()

    highest.__setitem__(0,30)



    for i,beam in enumerate(beams):
        # for j,beam_y in enumerate(beams):
        #     if beam is not beam_y:
        #         if beam:
        # beams.super_colide()
        if i<len(beams)-5 and beam.body.position.y > highest[0]:
            highest[0] = beam.body.position.y
            score += 0.1
        beam.draw_poly(screen,camera)

    av = 0.99
    an = 0.01

    camera.x = (-(player.body.position.x))*(1-av) + camera.x*(av)
    camera.y = -300
    camera.scale = (((300/(highest[0]+200))**0.6)/1.3)*(an) + camera.scale*(1-an)

    highest.__setitem__(0,0)

    print(camera.scale)
    draw_ui(screen,score)

    time_ = time()

    # ground.draw_poly(screen)

    ...

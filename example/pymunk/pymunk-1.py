import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk

def add_ball(space):
    mass = 1
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius) # 1
    body = pymunk.Body(mass, inertia) # 2
    x = random.randint(120,380)
    body.position = x, 550 # 3
    shape = pymunk.Circle(body, radius) # 4
    space.add(body, shape) # 5
    return shape

def draw_ball(screen, ball):
    p = int(ball.body.position.x), 600-int(ball.body.position.y)
    pygame.draw.circle(screen, THECOLORS["blue"], p, int(ball.radius), 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()
    running = True

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    balls = []

    ticks_to_next_ball = 10
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

        screen.fill(THECOLORS["white"])

        for ball in balls:
            draw_ball(screen, ball)

        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(50)

if __name__ == '__main__':
    sys.exit(main())

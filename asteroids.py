import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        positive_rotation_vector = self.velocity.rotate(angle)
        negative_rotation_vector = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        positive_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        negative_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        positive_asteroid.velocity = positive_rotation_vector * 1.2
        negative_asteroid.velocity = negative_rotation_vector * 1.2

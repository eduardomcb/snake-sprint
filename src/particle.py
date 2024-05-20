import pygame
import random

from src.config import PARTICLE_RADIUS_MIN, PARTICLE_RADIUS_MAX, PARTICLE_SPEED_MIN, PARTICLE_SPEED_MAX, \
    PARTICLE_LIFETIME_MAX, PARTICLE_LIFETIME_MIN


class Particle:
    def __init__(self, pos, color):
        self.x, self.y = pos
        self.color = color
        self.radius = random.randint(PARTICLE_RADIUS_MIN, PARTICLE_RADIUS_MAX)
        self.dx = random.uniform(PARTICLE_SPEED_MIN, PARTICLE_SPEED_MAX)
        self.dy = random.uniform(PARTICLE_SPEED_MIN, PARTICLE_SPEED_MAX)
        self.lifetime = random.randint(PARTICLE_LIFETIME_MIN, PARTICLE_LIFETIME_MAX)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1
        self.radius = max(0, self.radius - 0.1)  # Diminuir o tamanho aos poucos

    def draw(self, surface):
        if self.lifetime > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

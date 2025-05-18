from ast import Tuple
import pygame

from settings import *

class Component:

    def __init__(self, rect: pygame.Rect):
        self.x: int = rect.x
        self.y: int = rect.y
        self.width: int = rect.width
        self.height: int = rect.height
        self.label = "Unnamed"

    def get_image_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen: pygame.Surface, crop_rect: pygame.Rect, offset_x: int, offset_y: int):
        screen_x = crop_rect.x + (self.x - offset_x)
        screen_y = crop_rect.y + (self.y - offset_y)
        rect = pygame.Rect(screen_x, screen_y, self.width, self.height)

        if crop_rect.colliderect(rect):
            pygame.draw.rect(screen, (255, 255, 0), rect, 2)



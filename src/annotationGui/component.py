import math
import pygame

from .settings import *

class Component:

    def __init__(self, rect: pygame.Rect, originalZoom: float, label="Unnamed", duration ='Unknown-Duration'):
        self.x: int = rect.x
        self.y: int = rect.y
        self.width: int = rect.width
        self.height: int = rect.height
        self.initZoom: float = originalZoom
        self.label = label
        self.duration = duration
        self.rect = rect
        self.color = GREEN

    def get_image_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.wdth, self.height)

    def draw(self, screen: pygame.Surface, crop_rect: pygame.Rect, offset_x: int, offset_y: int, zoom: float):
        if zoom == self.initZoom:
            screen_x = crop_rect.x + (self.x - offset_x)
            screen_y = crop_rect.y + (self.y - offset_y) 
        else:
            screen_x = crop_rect.x + ((self.x / self.initZoom * zoom) - offset_x)
            screen_y = crop_rect.y + ((self.y / self.initZoom * zoom) - offset_y) 

        screen_width = self.width * zoom
        screen_height = self.height * zoom

        self.rect = pygame.Rect(screen_x, screen_y, screen_width, screen_height)

        if crop_rect.colliderect(self.rect):
            pygame.draw.rect(screen, self.color, self.rect, 2)
            
            font = pygame.font.SysFont(None, 20)
            label_surface = font.render(self.label+", "+self.duration, True, self.color)
            label_rect = pygame.Rect(self.rect.x, self.rect.y-23, label_surface.get_rect().width+3, label_surface.get_rect().height+3)
            
            pygame.draw.rect(screen, (0,0,0), label_rect)
            screen.blit(label_surface, (self.rect.x, self.rect.y - 20))
            

    def update(self):
        if self.label in CLEF_TYPES:
            self.duration = 'Clef'

        if self.duration == 'Clef' and self.label not in CLEF_TYPES:
            self.duration = "Unknown-Duration"

    def export(self) -> dict:
        data = {
            "label": self.label,
            "duration": self.duration,
            "x": self.x // self.initZoom,
            "y": self.y // self.initZoom,
            "width": self.width,
            "height": self.height 
            }
        return data


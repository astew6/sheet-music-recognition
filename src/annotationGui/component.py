import math
import pygame

from .settings import *

class Component:

    def __init__(self, rect: pygame.Rect, originalZoom: float, label="Unnamed", duration ='Unknown-Duration'):
        # position and size
        self.x: int = rect.x
        self.y: int = rect.y
        self.width: int = rect.width
        self.height: int = rect.height

        # Initial zoom level when the component was created
        self.initZoom: float = originalZoom

        # Metadata for the component
        self.label = label
        self.duration = duration

        # drawing stuff
        self.rect = rect
        self.color = GREEN

    def get_image_rect(self) -> pygame.Rect:
        # Pygame Rect representing the component's location and size
        # dependant on zoom level
        return pygame.Rect(self.x, self.y, self.wdth, self.height)

    def draw(self, screen: pygame.Surface, crop_rect: pygame.Rect, offset_x: int, offset_y: int, zoom: float):
        #  Draw the component to the screen, scaling and positioning based on zoom and offset
        
        # Calculate screen coordinates depending on whether zoom is at original level
        if zoom == self.initZoom:
            screen_x = crop_rect.x + (self.x - offset_x)
            screen_y = crop_rect.y + (self.y - offset_y) 
        else:  # Adjust coordinates according to zoom scaling
            screen_x = crop_rect.x + ((self.x / self.initZoom * zoom) - offset_x)
            screen_y = crop_rect.y + ((self.y / self.initZoom * zoom) - offset_y) 

        # Scale dimensions to match current zoom
        screen_width = self.width * zoom
        screen_height = self.height * zoom

        self.rect = pygame.Rect(screen_x, screen_y, screen_width, screen_height)

        if crop_rect.colliderect(self.rect): # only draw if in screen bounds 
            pygame.draw.rect(screen, self.color, self.rect, 2) 
            
            font = pygame.font.SysFont(None, 20)
            label_surface = font.render(f"{self.label} {self.duration}", True, self.color)
            label_rect = pygame.Rect(self.rect.x, self.rect.y-23, label_surface.get_rect().width+3, label_surface.get_rect().height+3)
            
            pygame.draw.rect(screen, (0,0,0), label_rect)
            screen.blit(label_surface, (self.rect.x, self.rect.y - 20))
            

    def update(self):
        # Update the duration based on the component's label.
        if self.label in CLEF_TYPES:
            self.duration = 'Clef'

        if self.duration == 'Clef' and self.label not in CLEF_TYPES:
            self.duration = "Unknown-Duration"

        if self.label == "Horizontal-Barline" or self.label == "Vertical-Barline":
            self.duration = ""

    def export(self) -> dict:
        # Export the component's data to a dictionary format, converting coordinates back to their original scale.
        data = {
            "label": self.label,
            "duration": self.duration,
            "x": self.x // self.initZoom,
            "y": self.y // self.initZoom,
            "width": self.width,
            "height": self.height 
            }
        return data


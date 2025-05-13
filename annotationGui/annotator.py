import pygame

from settings import *

class Annotator():

    def __init__(self, image: str, bounds: tuple = ImageBounds):
        self.image: pygame.image = pygame.image.load(image)
        self.scale: int = ...
        self.cropRect: pygame.Rect = pygame.rect.Rect(bounds[0],bounds[1],bounds[2],bounds[3])
        self.draw_rect: pygame.Rect = pygame.Rect(0, 0, self.cropRect.width, self.cropRect.height)

        # mouse tracking
        self.dragging: bool = False
        self.last_mouse_pos: tuple = ()


    def draw(self, screen: pygame.display):
        # Draw the image on screen
        screen.blit(self.image, self.cropRect, area=self.draw_rect)

    def update(self, event: pygame.event):

        # Start dragging
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.cropRect.collidepoint(event.pos):
                self.dragging = True
                self.last_mouse_pos = event.pos
            
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        # Update position while dragging
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            dx = event.pos[0] - self.last_mouse_pos[0]
            dy = event.pos[1] - self.last_mouse_pos[1]

            # Move the visible window into the image (crop shifts)
            self.draw_rect.x -= dx
            self.draw_rect.y -= dy

            # Clamp to image bounds so you don't scroll out of view
            self.draw_rect.x = max(0, min(self.image.get_width() - self.draw_rect.width, self.draw_rect.x))
            self.draw_rect.y = max(0, min(self.image.get_height() - self.draw_rect.height, self.draw_rect.y))

            self.last_mouse_pos = event.pos



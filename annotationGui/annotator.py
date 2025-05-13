import pygame

from settings import *

class Annotator():

    def __init__(self, image: str, bounds: tuple = ImageBounds):
        self.original_image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self.zoom: float = 1.0
        
        self.cropRect: pygame.Rect = pygame.rect.Rect(bounds[0],bounds[1],bounds[2],bounds[3])
        self.draw_rect: pygame.Rect = pygame.Rect(0, 0, self.cropRect.width, self.cropRect.height)

        # mouse tracking
        self.dragging: bool = False
        self.last_mouse_pos: tuple = ()
        self.offset_x = 0;
        self.offset_y = 0;

        # Update scaled image
        self.updateScaledImage()

    def updateScaledImage(self):
        # Scale the image based on the current zoom level
        width: int = int(self.original_image.get_width() * self.zoom)
        height: int = int(self.original_image.get_height() * self.zoom)
        self.scaled_image: pygame.Surface = pygame.transform.smoothscale(self.original_image, (width, height))
        self.scaled_rect: pygame.Rect = self.scaled_image.get_rect()
    
        
    def draw(self, screen: pygame.display):
        # Create a temporary surface for cropping
        cropped_surface = pygame.Surface(self.cropRect.size, pygame.SRCALPHA)

        # Calculate the part of the scaled image to draw
        image_area = pygame.Rect(self.offset_x, self.offset_y, self.cropRect.width, self.cropRect.height)

        # Draw the visible portion onto the cropped surface
        cropped_surface.blit(self.scaled_image, (0, 0), area=image_area)

        # draw the cropped surface to the screen
        screen.blit(cropped_surface, self.cropRect.topleft)

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
            self.offset_x -= dx
            self.offset_y -= dy

            self.clampOffset() # clamp image to keep in on screen

            self.last_mouse_pos = event.pos

        elif event.type == pygame.MOUSEWHEEL:
            self.zoomAtCenter(event.y)


    def zoomAtCenter(self, zoom_direction: int):
        """Zoom in or out, keeping the crop area centered."""
        old_zoom = self.zoom
        if zoom_direction > 0: zoom_factor = 1.1 
        else: zoom_factor = 0.9
        self.zoom *= zoom_factor

        # Clamp zoom
        self.zoom: float = max(0.1, min(10, self.zoom))

        # Calculate zoom center relative to image
        crop_center: tuple = (self.offset_x + self.cropRect.width // 2,
                       self.offset_y + self.cropRect.height // 2)

        # Update image scale
        self.updateScaledImage()

        # Adjust offset so zoom stays centered
        new_crop_center: tuple = (int(crop_center[0] * self.zoom / old_zoom), int(crop_center[1] * self.zoom / old_zoom))

        self.offset_x: int = new_crop_center[0] - self.cropRect.width // 2
        self.offset_y: int = new_crop_center[1] - self.cropRect.height // 2

        self.clampOffset()

    def clampOffset(self):
        max_x: int = max(0, self.scaled_image.get_width() - self.cropRect.width)
        max_y: int = max(0, self.scaled_image.get_height() - self.cropRect.height)
        self.offset_x: int = max(0, min(self.offset_x, max_x))
        self.offset_y: int = max(0, min(self.offset_y, max_y))
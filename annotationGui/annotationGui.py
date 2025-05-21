import pygame
from annotator import Annotator
from component import Component
from settings import *


class Screen():

    def __init__(self, image: str, width: int = WIDTH, height: int = HEIGHT, caption: str = 'annotation gui'):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)

        self.running = True
        self.annotator: Annotator = Annotator(image)
        self.components: Component = []

        self.drawing = False

        
    def start(self):

        # file loading here

        self.update()

    def draw(self):
        self.display.fill(WHITE)
        
        self.annotator.draw(self.display)

        # Draw all components
        for comp in self.components:
            comp.draw(self.display, self.annotator.cropRect, self.annotator.offset_x, self.annotator.offset_y, self.annotator.zoom)

        # Draw current temp rectangle
        if self.drawing and self.start_pos:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            end_pos = self.annotator.screenToImage(mouse_x, mouse_y)
            temp_rect = createRect(self.start_pos, end_pos)
            temp_comp = Component(temp_rect, self.annotator.zoom)
            temp_comp.draw(self.display, self.annotator.cropRect, self.annotator.offset_x, self.annotator.offset_y, self.annotator.zoom)

        
        pygame.display.update()
        

    def update(self):
        while self.running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 3 and self.annotator.cropRect.collidepoint(event.pos):
                self.start_pos = self.annotator.screenToImage(*event.pos)
                self.drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:
              if event.button == 3 and self.drawing:
                end_pos = self.annotator.screenToImage(*event.pos)
                rect = createRect(self.start_pos, end_pos)
                self.components.append(Component(rect, self.annotator.zoom))
                self.drawing = False
                self.start_pos = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_LCTRL and self.components != []:
                    self.components.pop()
            
            self.annotator.update(event)

          self.draw()
   
def main(imgPath: str):
    screen = Screen(imgPath)
    screen.start()
 
if __name__ == "__main__":
    main("alexs_music.jpg")

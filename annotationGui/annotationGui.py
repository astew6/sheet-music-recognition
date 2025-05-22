import pygame
from annotator import Annotator
from component import Component
from settings import *
import json
from pathlib import Path

class Screen():

    def __init__(self, image: str, width: int = WIDTH, height: int = HEIGHT, caption: str = 'annotation gui'):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)

        self.running = True
        self.filePath = image
        self.annotator: Annotator = Annotator(image)
        self.components: Component = []

        self.drawing = False

        
    def start(self):
        file_path = Path(self.filePath+".json")

        if file_path.exists():
            with open(self.filePath+".json", "r") as f:
                componentDict = json.load(f)
            for data in componentDict.values():
                rect = pygame.Rect(data["x"], data["y"], data["width"], data["height"])
                comp = Component(rect, 1.0, label=data.get("label", "Unnamed"))
                self.components.append(comp)

        self.update()

    def finish(self):
        with open(self.filePath+".json", "w") as f:
            componentsDict: dict = {}
            for x, component in enumerate(self.components):
                componentsDict[x] = component.export()

            json.dump(componentsDict, f, indent=2)

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
              self.finish()

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

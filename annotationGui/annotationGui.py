import pygame, pygame_gui
from annotator import Annotator
from component import Component
from settings import *
import json, sys
from pathlib import Path

class Screen():

    def __init__(self, image: str, width: int = WIDTH, height: int = HEIGHT, caption: str = 'annotation gui'):
        pygame.init()

        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)

        self.ui_init()

        self.running = True
        self.filePath = image
        self.annotator: Annotator = Annotator(image)
        self.components: Component = []
        self.currentComponent = None

        self.drawing = False

    def ui_init(self):
        self.manager = pygame_gui.UIManager((self.width, self.height))
        
        _label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((10, 40), (200, 30)),
            text="Select Note Type:",
            manager=self.manager
        )

        self.notePicker = pygame_gui.elements.UIDropDownMenu(
            options_list=VALID_NOTES,
            starting_option="C",
            relative_rect=pygame.Rect((10, 70), (200, 30)),
            manager=self.manager
        )

        
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
        sys.exit()

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

        self.manager.update(1/60)
        self.manager.draw_ui(self.display)
        
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

                  if event.button == 1:
                      for component in self.components: 
                          if component.rect.collidepoint(event.pos):
                              if self.currentComponent: self.currentComponent.color = YELLOW
                              self.currentComponent = component
                              self.currentComponent.color = RED

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
                    if event.key == pygame.K_BACKSPACE and self.currentComponent:
                        self.components.pop(self.components.index(self.currentComponent))
                        self.currentComonent = None

                if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.ui_element == self.notePicker:
                        if self.currentComponent:
                            self.currentComponent.label = event.text

                        
                
                self.manager.process_events(event)
                self.annotator.update(event)
            
            self.draw()
            
   
def main(imgPath: str):
    screen = Screen(imgPath)
    screen.start()
 
if __name__ == "__main__":
    main("alexs_music.jpg")

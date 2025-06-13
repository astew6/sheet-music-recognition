import pygame, pygame_gui
from .annotator import Annotator
from .component import Component
from .settings import *
import json
from pathlib import Path

class Screen():

    def __init__(self, image: str, display = pygame.display.set_mode((WIDTH, HEIGHT)), width: int = WIDTH, height: int = HEIGHT, caption: str = 'annotation gui'):
        pygame.init()

        self.width = width
        self.height = height
        self.display = display
        pygame.display.set_caption(caption)

        self.ui_init()

        self.running = True
        self.filePath = image
        # Annotator handles zoom, pan, and image display
        self.annotator: Annotator = Annotator(image)
        self.components: Component = [] # List of annotation components (boxes)
        self.currentComponent = None

        self.drawing = False

    def ui_init(self):
        self.manager = pygame_gui.UIManager((self.width, self.height))
        
        # Label for note picker
        _label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((guiBounds[2]//2-100, 40), (200, 30)),
            text="Select Note Type:",
            manager=self.manager
        )

        # Dropdown menu to select note types
        self.notePicker = pygame_gui.elements.UIDropDownMenu(
            options_list=VALID_NOTES+CLEF_TYPES,
            starting_option="C",
            relative_rect=pygame.Rect((guiBounds[2]//2-100, 70), (200, 30)),
            manager=self.manager
        )

        # Label for duration picker
        _label2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((guiBounds[2]//2-100, 110), (200, 30)),
            text="Select Duration:",
            manager=self.manager
        )

        # Dropdown menu to select note durations
        self.durationPicker = pygame_gui.elements.UIDropDownMenu(
            options_list=VALID_DURATIONS,
            starting_option="quarter-note",
            relative_rect=pygame.Rect((guiBounds[2]//2-100, 140), (200, 30)),
            manager=self.manager
        )



        
    def start(self):
        # Load saved annotation data if it exists
        file_path = Path(self.filePath)
        file_name = file_path.name
        json_path = Path("temp/"+file_name+".json")

        if json_path.exists():
            with open("temp/"+file_name+".json", "r") as f:
                componentDict = json.load(f)
            for data in componentDict.values():
                rect = pygame.Rect(data["x"], data["y"], data["width"], data["height"])
                comp = Component(rect, 1.0, label=data.get("label", "Unnamed"), duration=data.get("duration", "Unlabed-note"))
                self.components.append(comp)

    def finish(self):
        # Save all current annotation data to a JSON file
        with open('temp/'+Path(self.filePath).name+".json", "w") as f:
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

        self.manager.update(1/60) # Update UI elements
        self.manager.draw_ui(self.display) # Draw UI
        
        pygame.display.update()
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.finish()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Right-click start drawing if inside image area
                if event.button == 3 and self.annotator.cropRect.collidepoint(event.pos):
                    self.start_pos = self.annotator.screenToImage(*event.pos)
                    self.drawing = True

                if event.button == 1:
                    for component in self.components: 
                        if component.rect.collidepoint(event.pos) and component.rect.colliderect(self.annotator.cropRect):
                            if self.currentComponent: self.currentComponent.color = GREEN
                            self.currentComponent = component
                            self.currentComponent.color = RED

            elif event.type == pygame.MOUSEBUTTONUP:
                # Finish drawing rectangle and create a component
                if event.button == 3 and self.drawing:
                    end_pos = self.annotator.screenToImage(*event.pos)
                    rect = createRect(self.start_pos, end_pos)
                    if self.currentComponent: self.currentComponent.color = GREEN
                    self.currentComponent = Component(rect, self.annotator.zoom)
                    self.currentComponent.color = RED

                    self.components.append(self.currentComponent)
                    self.drawing = False
                    self.start_pos = None


            if event.type == pygame.KEYDOWN:
                # Ctrl+Z: undo last component
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_LCTRL and self.components != []:
                    self.components.pop()
                # Delete selected component
                if event.key == pygame.K_BACKSPACE and self.currentComponent:
                    self.components.pop(self.components.index(self.currentComponent))
                    self.currentComponent = None
            
            # Handle dropdown changes
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                # Change label
                if event.ui_element == self.notePicker:
                    if self.currentComponent:
                        self.currentComponent.label = event.text

                # Change duration
                if event.ui_element == self.durationPicker:
                    if self.currentComponent:
                        self.currentComponent.duration = NOTE_NUM[event.text]

                        
                
            self.manager.process_events(event)
            self.annotator.update(event)

        for component in self.components:
            component.update()
            
# Entry point for running the GUI
def main(imgPath: str):
    screen = Screen(imgPath)
    screen.start()
    while(screen.running):
        screen.update()
        screen.draw()
 
if __name__ == "__main__":
    main("alexs_music.jpg")

import pygame
from annotator import Annotator
from settings import *


class Screen():

    def __init__(self, image: str, width: int = WIDTH, height: int = HEIGHT, caption: str = 'annotation gui'):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(caption)

        self.running = True
        self.annotator = Annotator(image)

        
    def start(self):

        # file loading here

        self.update()

    def draw(self):
        self.display.fill(WHITE)
        
        self.annotator.draw(self.display)
        
        pygame.display.update()
        

    def update(self):
        while self.running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              self.running = False
            
            self.annotator.update(event)

          self.draw()
   
def main(imgPath: str):
    screen = Screen(imgPath)
    screen.start()
 
if __name__ == "__main__":
    main("alexs_music.jpg")

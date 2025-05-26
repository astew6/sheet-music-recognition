import pygame
import pygame_gui

from .. import Screen

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sheet Music to MusicXML")

manager = pygame_gui.UIManager((width, height))

openFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((100, 100), (200, 50)),
    text='Select Input File!',
    manager=manager
)

running = True
while running:
    for event in pygame.event.get():
        manager.process_events(event)
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == openFile:
                file_path = filedialog.askopenfilename()
                print(file_path)
    
    manager.update(1/60)

    screen.fill((255, 255, 255))  

    manager.draw_ui(screen)

    pygame.display.flip()
    

pygame.quit()
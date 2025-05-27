import pygame
import pygame_gui
from multiprocessing import Process

from ..annotationGui.annotationGui import Screen
from ..annotationGui.settings import *

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sheet Music to MusicXML")

manager = pygame_gui.UIManager((WIDTH, HEIGHT))

setInputFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 10), (WIDTH-20, 50)),
    text='Select Input File!',
    manager=manager
)

annotateFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 70), (WIDTH-20, 50)),
    text='Annotate file',
    manager=manager
)

setOutputFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 130), (WIDTH-20, 50)),
    text='select output file',
    manager=manager
)

inputFilePath = None
outputFilePath = None

state = 'main'
running = True
while running:
    if state == 'main':
        for event in pygame.event.get():
            manager.process_events(event)
        
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == setInputFile:
                    inputFilePath = filedialog.askopenfilename(
                        filetypes=[
                            ("Image files", "*.png *.jpg *.jpeg *.bmp"),
                            ("All files", "*.*")
                        ],
                        title="Select input image file"
                    )
                    print(inputFilePath)
            
                if event.ui_element == annotateFile and inputFilePath != '':
                    state = 'annotate'
            
                if event.ui_element == setOutputFile:
                    outputFilePath = filedialog.asksaveasfilename(
                        defaultextension=".xml",  # or whatever extension you want
                        filetypes=[("XML files", "*.xml"), ("All files", "*.*")],
                        title="Select output file"
                    )
                    print(outputFilePath)

    
        manager.update(1/60)

        screen.fill((255, 255, 255))  

        manager.draw_ui(screen)

        pygame.display.flip()

    elif state == 'annotate':
        annotateGui = Screen(inputFilePath, screen)
        annotateGui.start()
        while annotateGui.running:
            annotateGui.update()
            annotateGui.draw()

        state = 'main'
    

pygame.quit()
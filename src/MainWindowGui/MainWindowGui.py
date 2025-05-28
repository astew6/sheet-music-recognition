from pathlib import Path
import pygame
import pygame_gui

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

inputLabel = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((10, 70), (WIDTH-20, 50)),
    html_text="Please Select an Input file!",
    manager=manager
)

analyzeImage = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 130), (WIDTH-20, 50)),
    text='Analyze Image (TBD!)',
    manager=manager
)

annotateFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 190), (WIDTH-20, 50)),
    text='Annotate Image',
    manager=manager
)

setOutputFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 250), (WIDTH-20, 50)),
    text='Select Output File',
    manager=manager
)

outputLabel = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((10, 310), (WIDTH-20, 50)),
    html_text="Please Select an Output file!",
    manager=manager
)


exportXml = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 370), (WIDTH-20, 50)),
    text='Export to MusicXML (TBD!)',
    manager=manager
)

noInputFilePopup = None

inputFilePath = " "
outputFilePath = " "

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
                    if inputFilePath == '' :
                        inputLabel.html_text = "Please Select an Output file!"
                    else:
                        inputLabel.html_text = inputFilePath
                        inputLabel.rebuild()
            
                if event.ui_element == annotateFile:
                    if Path(inputFilePath).exists() and inputFilePath != '':
                        state = 'annotate'
                    else:
                        noInputFilePopup = pygame_gui.windows.UIMessageWindow(
                            rect=pygame.Rect((WIDTH/2-300, HEIGHT/2-300), (300, 200)),
                            window_title='No Input File Selected',
                            html_message='Please Select an Input File!',
                            manager=manager
                        )
            
                if event.ui_element == setOutputFile:
                    outputFilePath = filedialog.asksaveasfilename(
                        defaultextension=".xml", 
                        filetypes=[("XML files", "*.xml"), ("All files", "*.*")],
                        title="Select output file"
                    )
                    outputLabel.html_text = outputFilePath
                    outputLabel.rebuild()
                
            if event.type == pygame_gui.UI_WINDOW_CLOSE:
                if event.ui_element == noInputFilePopup:
                    noInputFilePopup = None  

    
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

    elif state == "export":
        pass
    

pygame.quit()
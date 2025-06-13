from pathlib import Path
import pygame
import pygame_gui

from ..annotationGui.annotationGui import Screen
from ..annotationGui.settings import *

from ..exportMusicXML.decipherNotes import decipherNotes
from ..exportMusicXML.exportMusicXML import exportXML

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sheet Music to MusicXML")

manager = pygame_gui.UIManager((WIDTH, HEIGHT), "src/MainWindowGui/theme.json")

# Constants for layout
MARGIN_X = 10
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 50
SECTION_GAP = 40
SMALL_GAP = 20
LABEL_HEIGHT = 30

BACKGROUND_COLOR = (37, 41, 46)

# Title label at top of screen
title_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((WIDTH//2 - 350, 20), (700, 90)),
    text="SHEET MUSIC TO MUSICXML",
    manager=manager,
    object_id=pygame_gui.core.ObjectID(object_id='title_label')
)

# Main Container 
main_container = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((140, 100), (1000, 550)),
    starting_height=1,
    manager=manager
)

# Top Buttons Container
top_buttons = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((20, 20), (960, 100)),
    starting_height=2,
    manager=manager,
    container=main_container
)

setInputFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 10), (460, 80)),
    text='Upload Picture',
    manager=manager,
    container=top_buttons
)
setOutputFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((480, 10), (460, 80)),
    text='Set Output File',
    manager=manager,
    container=top_buttons
)

# Input Path and Progress
inputLabel = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((20, 130), (960, 30)),
    html_text='Input Path:',
    manager=manager,
    container=main_container
)

progress_bar = pygame_gui.elements.UIProgressBar(
    relative_rect=pygame.Rect((20, 170), (960, 30)),
    manager=manager,
    container=main_container
)

# Middle Buttons - Analyze / Annotate 
middle_buttons = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((20, 220), (960, 100)),
    starting_height=2,
    manager=manager,
    container=main_container
)

analyzeImage = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 10), (460, 80)),
    text='Analyze (TBD!)',
    manager=manager,
    container=middle_buttons
)

annotateFile = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((480, 10), (460, 80)),
    text='Annotate',
    manager=manager,
    container=middle_buttons
)

# Output Path 
outputLabel = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect((20, 340), (960, 30)),
    html_text='Output Path:',
    manager=manager,
    container=main_container
)

# Bottom Buttons - Output Path / Export
bottom_buttons = pygame_gui.elements.UIPanel(
    relative_rect=pygame.Rect((20, 380), (960, 100)),
    starting_height=2,
    manager=manager,
    container=main_container
)

exportXml = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0, 10), (950, 80)),
    text='Export MusicXML (TBD!)',
    manager=manager,
    container=bottom_buttons
)


noInputFilePopup = None

inputFilePath = ""
outputFilePath = ""

def createPopup(title: str, text: str):
    return pygame_gui.windows.UIMessageWindow(
        rect=pygame.Rect((WIDTH/2-300, HEIGHT/2-300), (300, 200)),
        window_title=title,
        html_message=text,
        manager=manager
    )

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
                        inputLabel.html_text = "Input Path: "
                    else:
                        inputLabel.html_text = "Input Path: " + inputFilePath
                    inputLabel.rebuild()
            
                if event.ui_element == annotateFile:
                    if Path(inputFilePath).exists() and inputFilePath != '':
                        state = 'annotate'
                    else:
                        noInputFilePopup = createPopup('No Input File Selected', 'Please Select an Input File!')
            
                if event.ui_element == setOutputFile:
                    outputFilePath = filedialog.asksaveasfilename(
                        defaultextension=".xml", 
                        filetypes=[("XML files", "*.xml"), ("All files", "*.*")],
                        title="Select output file"
                    )
                    if outputFilePath == '' :
                        outputLabel.html_text = "Output Path: "
                    else:
                        outputLabel.html_text = "Output Path: " + outputFilePath
                    outputLabel.rebuild()


                if event.ui_element == analyzeImage:
                    if Path(inputFilePath).exists() and inputFilePath != '':
                        #
                        # analyzing image code
                        #
                    
                        decipherNotes(inputFilePath)
                        analyzingFinished = createPopup('Image Analyzing', 'Image Analyzing has finished')
                    else:
                        noInputFilePopup = createPopup('No Input File Selected', 'Please Select an Input File!')

                if event.ui_element == exportXml:
                    if outputFilePath != '':
                        exportXML(inputFilePath, outputFilePath)
                        exportedPopup = createPopup('Exported To MusicXML', f'MusicXML file has been created at {outputFilePath}')
                    else:
                        noOutputFilePopup = createPopup('No Output File Selected', 'Please Select an Output MusicXML File!')
                
            if event.type == pygame_gui.UI_WINDOW_CLOSE:
                if event.ui_element == noInputFilePopup:
                    noInputFilePopup = None  

    
        manager.update(1/60)

        screen.fill(BACKGROUND_COLOR)  

        manager.draw_ui(screen)

        pygame.display.flip()

    elif state == 'annotate':
        annotateGui = Screen(inputFilePath, screen)
        annotateGui.start()
        while annotateGui.running:
            annotateGui.update()
            annotateGui.draw()

        state = 'main'
        decipherNotes(inputFilePath)

    elif state == "export":
        pass
    

pygame.quit()
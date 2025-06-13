import pygame

pygame.font.init()

# color constants 
WHITE: tuple = (255,255,255)
GREEN: tuple = (0,255,0)
YELLOW: tuple = (255,255,0)
RED: tuple = (255,0,0)

# screen dimensions
WIDTH: int = 1280
HEIGHT: int = 720

# Bounds
guiBounds: tuple = (0,10,300,HEIGHT-10)
ImageBounds: tuple = (300,10,WIDTH-300-10,HEIGHT-10-10)

# helper function to create rect
def createRect(start, end) -> pygame.Rect:
    x1, y1 = start
    x2, y2 = end
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return pygame.Rect(left, top, width, height)

# notes, can also include rests horiz lines and vert lines
VALID_NOTES: list = [
    "C", "C#/Db", "D", "D#/Eb", "E", "F",
    "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B", "Rest", "Horizontal-Barline", "Vertical-Barline"
    ]

# list of valid durations
VALID_DURATIONS: list = [
        "whole-note",      
        "half-note",
        "quarter-note",
        "eighth-note",
        "16th-note",
        "32nd-note",
        "64th-note",
    ]

# gui label -> export label map
NOTE_NUM: dict = {
    "whole-note": "1",      
    "half-note": "1/2",
    "quarter-note": "1/4",
    "eighth-note": "1/8",
    "16th-note": "1/16",
    "32nd-note": "1/32",
    "64th-note": "1/64"
    }

CLEF_TYPES: list = [
        "treble",               # G clef on 2nd line
        "french_violin",        # G clef on 1st line
        "bass",                 # F clef on 4th line
        "baritone_f",           # F clef on 3rd line 
        "subbass",              # F clef on 5th line
        "alto",                 # C clef on 3rd line
        "tenor",                # C clef on 4th line
        "baritone_c",           # C clef on 5th line
        "mezzo_soprano",        # C clef on 2nd line
        "soprano",              # C clef on 1st line
        "percussion",           # drum clef
        "tab",                  # guitar/bass tab
    ]

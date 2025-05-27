import pygame

pygame.font.init()

WHITE: tuple = (255,255,255)
YELLOW: tuple = (255,255,0)
RED: tuple = (255,0,0)

WIDTH: int = 1280
HEIGHT: int = 720

ImageBounds: tuple = (300,10,WIDTH-300-10,HEIGHT-10-10)

def createRect(start, end) -> pygame.Rect:
    x1, y1 = start
    x2, y2 = end
    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return pygame.Rect(left, top, width, height)

VALID_NOTES: list = [
    "C", "C#/Db", "D", "D#/Eb", "E", "F",
    "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"
    ]
    
"""
musicxml_data = {
    "pitches": [
        "C", "C#", "D", "D#", "E", "F",
        "F#", "G", "G#", "A", "A#", "B"
    ],
    "steps": ["A", "B", "C", "D", "E", "F", "G"],  # MusicXML <step>
    "alterations": {
        "natural": 0,
        "sharp": 1,
        "flat": -1,
        "double-sharp": 2,
        "double-flat": -2
    },
    "durations": [
        "whole",       # <type>whole</type>
        "half",
        "quarter",
        "eighth",
        "16th",
        "32nd",
        "64th"
    ],
    "rests": [  # MusicXML <rest/>
        "whole",
        "half",
        "quarter",
        "eighth",
        "16th",
        "32nd"
    ],
    "clefs": [  # MusicXML <clef> types
        {"sign": "G", "line": 2},  # Treble
        {"sign": "F", "line": 4},  # Bass
        {"sign": "C", "line": 3},  # Alto
        {"sign": "C", "line": 4},  # Tenor
        {"sign": "percussion", "line": 2}  # Percussion
    ],
    "time_signatures": [  # <time>
        {"beats": 4, "beat-type": 4},
        {"beats": 3, "beat-type": 4},
        {"beats": 6, "beat-type": 8},
        {"beats": 12, "beat-type": 8},
        {"beats": 5, "beat-type": 4}
    ],
    "articulations": [  # <articulations>
        "staccato",
        "accent",
        "tenuto",
        "strong-accent",
        "fermata"
    ],
    "dynamics": [  # <dynamics>
        "pp", "p", "mp", "mf", "f", "ff",
        "crescendo", "diminuendo"
    ],
    "tuplet_types": [  # <time-modification>
        "triplet", "quintuplet", "septuplet"
    ]
}
"""
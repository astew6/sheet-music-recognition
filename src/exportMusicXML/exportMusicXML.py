import json
from pathlib import Path
from .settings import *
from .decipherNotes import *
from music21 import stream, note, bar, meter, clef, key


def getValues(values, items):
    return [v for v in values if values[v]['label'] in items]

def sortValues(items, key):
    return sorted(items, key=lambda x: x[key])

def noteToPitch(label):
    pitch_map = {
        'E': 'E4',
        'F': 'F4',
        'G': 'G4',
        'A': 'A4',
        'B': 'B4',
        'C': 'C5',
        'D': 'D5',
        'E': 'E5',
        'F': 'F5'
    }
    return pitch_map.get(label.upper(), 'C4')  # default fallback


def exportXML(filePath, outputFilePath):
    values = loadJson(filePath)
    # hLines = sortItems(getValues(values, ['Horizontal-Barline']), 'y')
    vLines = sortItems(getItems(values, ['Vertical-Barline']), 'x')
    notes = sortItems(getItems(values, NOTES), 'x')

    # Build music21 score
    score = stream.Score()
    part = stream.Part()

    # Optional: add clef, key, time signature
    part.append(clef.TrebleClef()) # needs to change
    part.append(key.KeySignature(0))  # C major / A minor
    part.append(meter.TimeSignature('4/4')) # needs to change

    # Add notes to measure(s)
    m = stream.Measure()
    for n in notes:
        pitch = noteToPitch(n['label'])
        duration = get_duration(n['duration'])
        m.append(note.Note(pitch, type=duration))
    part.append(m)

    # Add barlines
    for vbar in vLines:
        m.append(bar.Barline(type='regular'))

    score.append(part)
    score.write('musicxml', fp=outputFilePath)


def get_duration(label):
    if label == '1':
        return 'whole'
    elif label == '1/2':
        return 'half'
    elif label == '1/4':
        return 'quarter'
    elif label == '1/8':
        return 'eighth'
    elif label == '1/16':
        return '16th'
    elif label == '1/32':
        return '32nd'
    else:
        return 'quarter'  # default fallback
    

if __name__ == "__main__":
    # exportXML("alexs_music.jpg")

    decipherNotes("alexs_music.jpg")
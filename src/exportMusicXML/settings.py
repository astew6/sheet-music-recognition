import json
from pathlib import Path


# A list of all musical note labels 
NOTES: list = [
    "C", "C#/Db", "D", "D#/Eb", "E", "F",
    "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B", "Unnamed"
    ]

# Notes found on barlines
barlineNotes: list = [
    "F", "D", "B", "G", "E"
    ]

# Notes found in the spaces between staff lines
spacingNotes: list = [
    "E", "C", "A", "F"
    ]

# A basic rectangle class 
class Rect:

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 

    # Check if a point (x, y) lies within the rectangle
    def collidePoint(self, point: tuple) -> bool:
        px, py = point
        return (self.x <= px < self.x + self.width) and (self.y <= py < self.y + self.height)

    # Check if a y-value falls within the vertical bounds of the rectangle
    def collidePointY(self, y: int) -> bool:
        return (self.y <= y < self.y + self.height)

    def toString(self):
        return f"x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}"

# Load JSON data from a given file path if it exists in the "temp" directory
def loadJson(filePath: str):
    file_path = Path(filePath)
    file_name = file_path.name
    json_path = Path("temp/"+file_name+".json")

    if json_path.exists():
        with open("temp/"+file_name+".json", "r") as f:
            return json.load(f)

    else: print("File Does Not Exist")

# Return all dictionary entries from values that have a label matching one of items
def getItems(values: dict, items: list = []):
    return_vals = []
    for value in values:
        current = values[value]
        if current['label'] in items:
            return_vals.append(current)

    return return_vals

# Sort dictionary entries by a key and return them in sorted order
def sortItems(values: dict, item):
    item_list = []
    return_vals = []
    for value in values:
        item_list.append(value[item])

    item_list.sort()
    for i in item_list:
        for value in values:
            if i == value[item]:
                return_vals.append(value)

    return return_vals

# Replace oldData with newData in the values dict
def setData(values: dict, oldData: dict, newData: dict):
    oldValues = values.copy()
    for value in oldValues:
        current = oldValues[value]
        if current == oldData:
            values[value] = newData
import json
from pathlib import Path

NOTES: list = [
    "C", "C#/Db", "D", "D#/Eb", "E", "F",
    "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B", "Unnamed"
    ]

barlineNotes: list = [
    "F", "D", "B", "G", "E"
    ]

def loadJson(filePath: str):
    file_path = Path(filePath)
    file_name = file_path.name
    json_path = Path(file_name + ".json")

    if json_path.exists():
        with open(file_name+".json", "r") as f:
            return json.load(f)

    else: print("File Does Not Exist")

def getItems(values: dict, items: list = []):
    return_vals = []
    for value in values:
        current = values[value]
        if current['label'] in items:
            return_vals.append(current)

    return return_vals

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

class Barline():

    def __init__(self, line: dict):
        self.lines = line
        self.centerx = (line['x'] + line['width']) // 2
        self.centery = (line['y'] + line['height']) // 2
        self.width = int(line['width'])
        self.height = int(line['height'])
        self.staffNote = None

    def toString(self) -> str:
        return f"center: ({self.centerx}, {self.centery}) | note: {self.staffNote}"

class Note():

    def __init__(self, dictVal: dict):
        self.dictVal = dictVal
        self.centerx = (dictVal['x'] + dictVal['width']) // 2
        self.centery = (dictVal['y'] + dictVal['height']) // 2
        self.top = self.y
        self.bottom = self.y+self.height
        self.duration = dictVal['duration']
        self.name = dictVal['label']

    def toString(self) -> str:
        return f"Name: {self.name}, Position: ({self.centerx}, {self.centery}), Duration: {self.duration}"

def catagorizeNote(note, hLines: list):
    previousLine = None
    noteGap = (hLines[0][1].centery - hLines[0][0].centery) // 2

    for group in hLines:
        if group[0].centery < note.centery and group[len(group)-1].centery > note.centery:
            for i, line in enumerate(group):
                if abs(line.centery - note.centery) <= noteGap:
                    note.name = line.staffNote
     
    return False 
def parseBarlines(line_type, specifier, values):
    lines = sortItems(getItems(values, items=[line_type]), specifier)
    retLines = []
    temp = []
    previousLine = Barline(lines[0])
    for j in lines:
        currentLine = Barline(j)
        if currentLine.centery > previousLine.centery+50: # need to create calibration sequence
            retLines.append(temp)
            temp=[]

        temp.append(currentLine)
        previousLine = currentLine

    retLines.append(temp)
    for i in retLines:
        catagorizeBarlines(i)

    return retLines

def catagorizeBarlines(lines): # need to implement ledger lines
    for i, line in enumerate(lines):
        line.staffNote = barlineNotes[i]


class exportXML():

    def __init__(self, filePath):
        self.values = loadJson(filePath)
        self.hLines = parseBarlines('Horizontal-Barline','y', self.values)
        self.vLines = sortItems(getItems(self.values, items=['Vertical-Barline']), 'x')
        notes = getItems(self.values, NOTES)
        for i in self.hLines:
            for j in i:
                print(j.toString())
            print(" ")
        self.notes = []
        
        for i in notes:
            self.notes.append(Note(i))
        
        for i in self.notes:
            catagorizeNote(i,self.hLines)
            print(i.toString())
        

    

if __name__ == "__main__":
    exportXML("alexs_music.jpg")
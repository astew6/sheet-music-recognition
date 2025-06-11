from .settings import *


class Barline():

    def __init__(self, line: dict):
        self.line = line
        self.centerx = (line['x'] + line['width'] // 2)
        self.centery = (line['y'] + line['height'] // 2) 
        self.width = int(line['width'])
        self.height = int(line['height'])
        self.staffNote = None

    def toString(self) -> str:
        return f"center: ({self.centerx}, {self.centery}) | note: {self.staffNote}"

class Note():

    def __init__(self, dictVal: dict):
        self.dictVal = dictVal
        self.centerx = (dictVal['x'] + dictVal['width'] // 2) 
        self.centery = (dictVal['y'] + dictVal['height'] // 2) 
        self.rect: Rect = Rect(self.centerx, self.centery, dictVal['width'], dictVal['height'])
        self.duration = dictVal['duration']
        self.name = dictVal['label']

    def toString(self) -> str:
        return f"Name: {self.name}, Position: ({self.centerx}, {self.centery}), Duration: {self.duration} | Rect: {self.rect.toString()}"

def catagorizeNote(note, hLines: list):
    noteGap = (hLines[0][1].centery - hLines[0][0].centery) // 2

    for group in hLines:
        for i, line in enumerate(group):
            if i < len(group)-1:
                if note.rect.collidePointY(line.centery) and note.rect.collidePointY(group[i+1].centery):
                    note.name = spacingNotes[barlineNotes.index(line.staffNote)]
                elif note.rect.collidePointY(line.centery):
                    note.name = line.staffNote
                #if abs(line.centery - note.centery) <= (noteGap//2): 
                #    note.name = line.staffNote
                #elif abs(line.centery - note.bottom) <= noteGap and abs(group[i-1] - note.top) <= noteGap:
                #    note.name = spacingNotes[barlineNotes.index(line.staffNote)-1]

            else:
                if note.rect.collidePointY(line.centery):
                    note.name = line.staffNote

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

def decipherNotes(filePath: str):
    values = loadJson(filePath)
    hLines = parseBarlines('Horizontal-Barline','y', values)
    vLines = sortItems(getItems(values, items=['Vertical-Barline']), 'x')
    
    #for i in hLines:
    #    for j in i:
    #        print(j.toString())
    #    print(" ")
    
    Notes = getItems(values, NOTES)
    notes = []
    for i in Notes:
        notes.append(Note(i))
        
    for i in notes:
        if i.name == "Unnamed":
            catagorizeNote(i,hLines)

    for group in hLines:
        for line in group:
            line.line['duration'] = line.staffNote
        
    exportNotes(values, notes, filePath)

def exportNotes(values: dict, notes, filePath):
    for note in notes:
        newNote = note.dictVal.copy()
        newNote['label'] = note.name
        setData(values, note.dictVal, newNote)
    
    with open('temp/'+Path(filePath).name+".json", "w") as f: # need to change this
        json.dump(values, f, indent=2)

if __name__ == "__main__":
    decipherNotes("alexs_music.jpg")
import json
from pathlib import Path

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

def sortItems(values: dict, item: str):
    ...

class exportXML():

    def __init__(self, filePath):
        self.values = loadJson(filePath)
        self.hLines = getItems(self.values, items=['Horizontal-Barline'])
        self.vLines = getItems(self.values, items=['Vertical-Barline'])


if __name__ == "__main__":
    exportXML("alexs_music.jpg")
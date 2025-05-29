# Sheet Music Recognition

An application designed for the easy and automated transcripiton of a page of paper sheet music into a digital MusicXML file.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
        <a href="#about-the-project">About The Project</a>
    </li>
    <li>
        <a href="#getting-started">Getting Started</a>
    </li>
    <li>
        <a href="#roadmap">Roadmap</a>
    </li>
  </ol>
</details>

# About The Project

This application is being created at the request of Mr. Emond to assist is his teaching so that he doesn't have to spend as much time transcribing sheet music into the computer.

# Getting Started
1. Clone this repositiory to your local machine.
2. Double click the run.bat file 
   - this will create a .venv and download the dependencies with pip
   - will also create a temp directory if there is not already one
3. after all nessesary files/folders are downloaded/created the program will run and you can use the app
   - NOTE - check the <a href="###current-functionality">Implemented Features</a> to make sure eveyrthing is functioning properly

### TLDR Just Double Click the run.bat file and the app will start
- Make sure you have pip and python 3.8+ installed!

# Roadmap
### Current Functionality:
- can load images and set output xml files
- can check the <a href="#annotator-gui">annotate images</a> by creating fields (green boxes) and label them using the GUI
   - EX: Drawing a field around a treble clef and using the GUI to label it as a Treble Clef
- annotations will be saved in a temp directory

![Current Functionality](design/readme-images/main-frame.png?raw=true "Current Functionality")
 
### To Be Implemented:
- Analyzing images through image recognition (Alex is training the AI)
   - Ai will analyze sheet music and create annotations and store them in a temp directory (Annotator can access if need)
- Exporting Annotated images (stored in JSON files) to MusicXML fies
   - Sarvesh is currently learning about this but by the end of sprint 4 there will be functionality to export annotations to musicXML files

* current projected first beta release may 14 2025 

# Annotator GUI
This is a gui for the user to check if the AI has recognized all the elements (AI not implemented yet)

#### Image navigation:
- left click and drag to pan around image
- scroll wheel to zoom in and out

#### Field management 
- To create fields, hold right click and drag. 
   - (all fields will be labeled as "Unlabled, Unknown-duration" by default)
- Two dropdown menus on left side of screen to change label and duration
   - Any label that is a clef will automatically remove the duration

![Annotation GUI](design/readme-images/annotation-gui.png?raw=true "Annotation Gui")

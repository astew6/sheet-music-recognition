import numpy as np
import cv2

def getFile(filePath: str):
    return cv2.imread(filePath)

img = getFile("alexs_music.jpg");
img = cv2.resize(img, (0, 0), fx = 0.3, fy = 0.3)

# convert the image to a binary image (only black and white) to make it easier for image detection
_, binaryImage = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# this looks in the binary iamge for any vertical lines
# it is looking for a rectangle that is 1 pixel long and 50 pixels tall
lines = cv2.morphologyEx(binaryImage, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (10, 1)), iterations=1)

# takes the lines found and tries to actuall find perfectly vertical lines 
# outputs a 2d matrix to vertical lines that includ the start and end bounds of each vertical line [[x1,y1,x2,y2],[...],[...]]
horizontal_lines = cv2.HoughLinesP(lines, 1, np.pi / 180, threshold=200, minLineLength=10, maxLineGap=5) 

output = img.copy() # create a copy of the image to write on
if lines is not None: # only draw lines on image if there are lines
    for line in horizontal_lines:
        x1, y1, x2, y2 = line[0] # get the bounds of the line
        cv2.line(output, (x1, y1), (x2, y2), (0, 0, 255), 2) # draw a highlight on top of immge

# Show the image
cv2.imshow('detetect lines',output)
cv2.waitKey(0)
cv2.destroyAllWindows()


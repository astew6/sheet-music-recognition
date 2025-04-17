import numpy as np
import cv2

def getFile(filePath: str):
    return cv2.imread(filePath, 0) # reads image in grayscale

img = getFile("tempFile.jpg");

# Show the image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

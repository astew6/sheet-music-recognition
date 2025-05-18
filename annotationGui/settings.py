import pygame

WHITE: tuple = (255,255,255)

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
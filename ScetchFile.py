import random
import pygame
pygame.init()

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

infoObject = pygame.display.Info()
print(infoObject.current_w, infoObject.current_h)

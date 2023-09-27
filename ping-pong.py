from pygame import *
from random import randint

win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('piiiing-poooong')
background = transform.scale(
    image.load('images.jpg'),
    (win_width, win_height)
)
clock = time.Clock()
FPS = 60
run = True
while run:
    window.blit(background, (0, 0))
    display.update()
    clock.tick(FPS)
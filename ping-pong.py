from pygame import *
from random import randint

win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption('piiiing-poooong')
background = transform.scale(
    image.load('bg.jpg'),
    (win_width, win_height)
)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def updater(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
ball = GameSprite('donut228.png', 100, 100, 10, 65, 70)
homa1 = Player('homak.jpg', 0, 200, 10, 65, 70)
homa2 = Player('homak.jpg', 630, 300, 10, 65, 70)
clock = time.Clock()
FPS = 60
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    ball.reset()
    homa1.updater()
    homa1.reset()
    homa2.updatel()
    homa2.reset()
    display.update()
    window.blit(background, (0, 0))
    clock.tick(FPS)

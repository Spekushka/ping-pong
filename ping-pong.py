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
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render("PLAYER 1 LOSE!", True, (180, 0, 0))

font2 = font.Font(None, 35)
lose2 = font2.render("PLAYER 2 LOSE!", True, (180, 0, 0))

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
ball = GameSprite('donut228.png', 100, 100, 10, 50, 50)
homa1 = Player('homak.jpg', 0, 250, 10, 15, 100)
homa2 = Player('homak.jpg', 685, 250, 10, 15, 100)
clock = time.Clock()
FPS = 60
run = True
finish = False

speed_x = 3
speed_y = 3
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    window.blit(background, (0, 0))
    ball.reset()
    homa1.updater()
    homa1.reset()
    homa2.updatel()
    homa2.reset()
    if sprite.collide_rect(homa1, ball) or sprite.collide_rect(homa2, ball):
        speed_x *= -1
    if ball.rect.y > win_height- 50 or ball.rect.y < 0:
        speed_y *= -1  

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > win_width-50:
        finish = True
        window.blit(lose2, (200, 200))
    display.update()
    
    clock.tick(FPS)

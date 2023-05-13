from pygame import *
from random import randint
finish = False
game = True
clock = time.Clock()
fps = 45


win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('ПИНГ-ПОНГ')
background = transform.scale(image.load("fo1.jpg"),(win_width, win_height))

"""class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height -80:
            self.rect.y += self.speed
    def update_r(self):
        keys = keys.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += self.speed
            pravayaraketa = Player('images.jpg', 30,200,4,50,150)
            levayaunitaz = Player('Без названия.jpg', 520,200,4,50,150)
            ball = GameSprite('zelenka.jpg',200,200,4,50,50 )"""
while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:

        window.blit(background, (0,0))

    display.update()
    clock.tick(fps)
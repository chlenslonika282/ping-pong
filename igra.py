from pygame import *
from random import randint
font.init()
finish = False
game = True
clock = time.Clock()
fps = 165


win_width = 700
win_height = 500

speed_x = 3
speed_y = 3
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSE!", True, (100, 0, 0))
window = display.set_mode((win_width, win_height))
display.set_caption('ПИНГ-ПОНГ')
background = transform.scale(image.load("fo1.jpg"),(win_width, win_height))

class GameSprite(sprite.Sprite):
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
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height -80:
            self.rect.y += self.speed
    def update_1(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += self.speed

pravayaraketa = Player('pravayaraketa.png', 30,200,4,50,150)
levayaunitaz = Player('pravayaraketa.png', 620,200,4,50,150)
ball = GameSprite('bLL.png',200,200,4,50,50 )

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        if finish != True:
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(pravayaraketa, ball) or sprite.collide_rect(levayaunitaz, ball):
            speed_x *= -1
        

        window.blit(background, (0,0))
        pravayaraketa.reset()
        levayaunitaz.reset()
        pravayaraketa.update_r()
        levayaunitaz.update_1()
        ball.reset()
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (250, 200))
        if ball.rect.x > 640:
            finish = True
            window.blit(lose2, (250, 200))

    display.update()
    clock.tick(fps)
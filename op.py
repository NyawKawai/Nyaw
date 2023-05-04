from pygame import *

width = 700
heignt =500

mc_x = 270
mc_y = 200
#окно
root = display.set_mode((width, heignt))
bg = transform.scale(image.load('futmych.jpg'),(width, heignt))

speed_x=3
speed_y= 3

class GameSprite(sprite.Sprite):
    #конструктор
    def __init__ (self, sprite_image, sprite_x,sprite_y,sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image),(160,100))
        self.speed = sprite_speed
        #хитбокс спрайта
        self.rect=self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    #перерисовка спрайта
    def redraw(self):
        root.blit(self.image, (self.rect.x,self.rect.y))
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
    
class Player1(GameSprite):
    def update(self):
        #получаем последние нажатые клавиши
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        elif keys[K_DOWN] and self.rect.y < heignt - 100:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        #получаем последние нажатые клавиши
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < heignt - 100:
            self.rect.y += self.speed


class Mc(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.side = True
        elif self.rect.x >= width - 85:
            self.side = False


mc = Mc('mc.png', 270, 200, 5)

player1 = Player1('klushka2.png', 80, 89, 5)
player2 = Player2('raketrka.png', 570, 89, 5)

#время для обнвл
clock = time.Clock()
game_on = True
while game_on:
    for e in event.get():
        if e.type == QUIT:
            game_on=False
    root.blit(bg,(0,0))

    mc.rect.x+=speed_x
    mc.rect.y+=speed_y
    if mc.rect.y <0 or mc.rect.y>heignt-70:
        speed_y*=-1
    
    if mc.rect.x>width-90 or mc.rect.x<0:
        speed_x*=-1


    player1.update()
    player1.redraw()

    player2.update()
    player2.redraw()

    mc.update()
    mc.redraw()

    if mc.colliderect(player1.rect):
        speed_x*=-1
    
    if mc.colliderect(player2.rect):
        speed_x*=-1
            


    #обновл экрана
    display.update()
    clock.tick(60)
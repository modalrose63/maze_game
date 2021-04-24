from pygame import *
from random import randint

window = display.set_mode((1080,720))
display.set_caption("Космическое приключение")

background = transform.scale(image.load("space.jpg"), (1080,720))


clock = time.Clock()

font.init()
font = font.SysFont("Ari", 70)
text = font.render(
   "Ты проиграл!", True, (0,0,0)
)
text2 = font.render(
   "Ты победил!", True, (0,0,0)
)


FPS = 60

y1 = 10
x1 = 10

y2 = 10
x2 = 10

finish = False

#mixer.init()
#mixer.music.load("jungles.ogg")
#mixer.music.play()



keys_pressed = key.get_pressed()

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))

        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
winz = Gamesprite("cookie.png",970 ,650 ,0)

class Player(Gamesprite):
    def update(self):
        
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y <670:
            self.rect.y += self.speed

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 1030:
            self.rect.x += self.speed

privedenie1 = Player("shrek_PNG40.png", 100, 100, 5)

class Enemy(Gamesprite):
    def update(self):
        if self.i < 50:
            self.rect.x -= self.speed
            self.i += 1
        if self.i >= 50 and self.i < 100:
            self.rect.y -= self.speed
            self.i += 1
        if self.i >= 100 and self.i < 150:
            self.rect.x += self.speed
            self.i += 1
        if self.i >= 150 and self.i < 200:
            self.rect.y += self.speed
            self.i += 1
        if self.i == 200:
            self.i = 0

        '''if self.rect.x <= 320:
            #self.direction = "right"
        if self.rect.x >= 500:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed'''
            
vrag = Enemy("alien_PNG64.png", 500,400, 3)
vrag.i = 0

class Wall(sprite.Sprite):
    def  __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

wall1 = Wall(255,255,255,100,200,10,420)

wall2 = Wall(255,255,255,100,200,100,10)

wall3 = Wall(255,255,255,190,0,10,200)

wall4 = Wall(255,255,255,200,300,10,500)

wall5 = Wall(255,255,255,300,200,10,400)

wall6 = Wall(255,255,255,200,200,100,10)

wall7 = Wall(255,255,255,300,600,200,10)

wall8 = Wall(255,255,255,600,100,10,700)

wall9 = Wall(255,255,255,400,500,400,10)

wall10 = Wall(255,255,255,300,200,200,10)

wall11 = Wall(255,255,255,300,100,300,10)

wall12 = Wall(255,255,255,700,0,10,400)

wall13 = Wall(255,255,255,900,100,10,700)

wall14 = Wall(255,255,255,700,600,200,10)

wall15 = Wall(255,255,255,700,400,100,10)

wall16 = Wall(255,255,255,800,300,100,10)

wall17 = Wall(255,255,255,700,200,100,10)

wall18 = Wall(255,255,255,800,100,100,10)



game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0, 0))

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        wall11.draw_wall()
        wall12.draw_wall()
        wall13.draw_wall()
        wall14.draw_wall()
        wall15.draw_wall()
        wall16.draw_wall()
        wall17.draw_wall()
        wall18.draw_wall()
        vrag.update()
        vrag.reset()
        winz.reset()
        privedenie1.update()
        privedenie1.reset()

        clock.tick(FPS)

        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and y1 > 5:
            y1 -= 5

        if keys_pressed[K_s] and y1 < 1075:
            y1 += 5

        if keys_pressed[K_a] and x1 > 5:
            x1 -= 5

        if keys_pressed[K_d] and x1 < 1075:
            x1 += 5

        if sprite.collide_rect (privedenie1, wall1):
            window.blit(text, (400, 300))
            window.blit(text2, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall2,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall3,):
            window.blit(text, (400, 300))
            finish = True
   
        if sprite.collide_rect(privedenie1, wall4,):
            window.blit(text, (400, 300))
            finish = True
        
        if sprite.collide_rect(privedenie1, wall5,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall6,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall7,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall8,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall9,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall10,):
            window.blit(text, (400, 300))
            finish = True
   
        if sprite.collide_rect(privedenie1, wall11,):
            window.blit(text, (400, 300))
            finish = True
        
        if sprite.collide_rect(privedenie1, wall12,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall13,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall14,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall15,):
            window.blit(text, (400, 300))
            finish = True
        
        if sprite.collide_rect(privedenie1, wall16,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall17,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, wall18,):
            window.blit(text, (400, 300))
            finish = True

        if sprite.collide_rect(privedenie1, vrag):
            finish = True
            window.blit(text, (400, 300))
        
        if sprite.collide_rect(privedenie1, winz):
            window.blit(text2, (400, 300))
            finish = True
   
        display.update()
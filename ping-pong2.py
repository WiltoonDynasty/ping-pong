from pygame import *
from time import time as timer

img_player = "player.png"
img_ball = "ball.png"
back = (232, 232, 232)

score1 = 0 
score2 = 0 
goal = 3 
lost = 0 



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, weight, height):
        super().__init__()
 
        self.image = transform.scale(image.load(player_image), (weight, height))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

#класс для спрайтов-препятствий
class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
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

win_width = 600
win_height = 500
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
window.fill(back)


font.init()
font = font.Font(None,80)

lose1 = font.render('PLAYER 1 LOSE!', True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True,(180,0,0))
win1 = font.render('PLAYER 1 WIN', True,(0, 255, 76))
win2 = font.render('PLAYER 2 WIN', True,(0, 255, 76))

speed_x = 3
speed_y = 3

game = True
finish = False
clock = time.Clock()
FPS = 60

ship = Player(img_player,3,200,4,50,150)
ship2 = Player(img_player,545,200,4,50,150)
ball = GameSprite(img_ball,200,200,4,50,50)

w1 = Wall(38, 37, 37, 300, 0, 10, 500)

run = True

rel_time = False

num_fire = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        window.fill(back)
        ship.update_r()
        ship2.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        w1.draw_wall()

        if sprite.collide_rect(ship,ball) or sprite.collide_rect(ship2,ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            score2 = score2 + 1
            ball = GameSprite(img_ball,200,200,4,50,50)
            #window.blit(lose1,(200,200))
            game_over = True

        if ball.rect.x > win_width:
            score1 = score1 + 1
            ball = GameSprite(img_ball,200,200,4,50,50)
            #window.blit(lose2,(200,200))
            game_over = True

        if score1 >= goal:
            finish = True
            window.blit(win1, (100, 200))

        if score2 >= goal:
            finish = True
            window.blit(win1, (100, 200))

        text = font.render(str(score1), 1, (38, 37, 37))
        window.blit(text, (250, 20))

        text = font.render(str(score2), 1, (38, 37, 37))
        window.blit(text, (330, 20))

        ship.reset()
        ship2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
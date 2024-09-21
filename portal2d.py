from pygame import *

import time as timers

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        self.image = transform.scale(image.load(player_image), (width, height))  
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y
        super().__init__()
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Rectangle(sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        super().__init__()
        self.isblocked = False
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

       

class Player(GameSprite):
    # рух гравця
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed [K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if key_pressed [K_a] and self.rect.x > 0:
            self.rect.x -= 5
        if key_pressed [K_s] and self.rect.y <Win_height - self.height:
            self.rect.y += 5
        if key_pressed [K_d] and self.rect.x <Win_width - self.width:
            self.rect.x += 5


    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__(player_image, x, y, width, height, speed)
        self.Portalgun = transform.scale(image.load('Portalgun.png'), (30, 16))
        self.cube = None
        

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.Portalgun, (self.rect.x + 20, self.rect.y + 20))
        if self.cube:
           window.blit(self.cube, (self.rect.x + 60, self.rect.y + 15))

class Bullet(GameSprite):
    def __init__(self, player_image, x, y, width, height, speed, x2, y2):
        super().__init__(player_image, x, y, width, height, speed)
        if level == 4 or level == 6:
            self.x_speed = ((x2 - x) * speed) / (((x2 - x)**2 + (y2 - y) ** 2) ** 0.5)
            self.y_speed = ((y2 - y) * speed) / (((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5)
        elif level == 5:
            self.x_speed = - speed
            self.y_speed = 0
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.x < 0 or self.rect.x > Win_width or self.rect.y < 0 or self.rect.y > Win_height:
            self.kill()

class Portal(GameSprite):
    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__(player_image, x, y, width, height, speed)
        self.rect.centerx = x
        self.rect.centery = y

class Turret(GameSprite):
    def shoot(self, speed = 10):
        bullets.add(Bullet("bullet.png", self.rect.centerx, self.rect.centery, 10, 10, speed, player.rect.centerx, player.rect.centery))

font.init()

mixer.init()

mixer.music.load("portal-radio-tune.mp3")

mixer.music.set_volume(0.2)

is_music = False

font1 = font.Font(None, 50)

level = 1

player = Player('Chell.png', 75, 65, 40, 32, 5)

turret = Turret('turret.png', 462, 25, 32, 32, 0)

turret2 = Turret('turret.png', 462, 626, 32, 32, 0)

turret3 = Turret('turret.png', 324, 14, 32, 32, 0)

turret4 = Turret('turret.png', 324, 51, 32, 32, 0)

turret5 = Turret('turret.png', 324, 88, 32, 32, 0)

turret6 = Turret('turret.png', 324, 125, 32, 32, 0)

turret7 = Turret('turret.png', 324, 162, 32, 32, 0)

turret8 = Turret('turret.png', 324, 199, 32, 32, 0)

GLaDOS = Turret('GLaDOS.png', 350, 259, 256, 200, 0)


lava = Rectangle(344, 0, 224, 700, (255, 147, 0))

wall1 = Rectangle(242, 0, 71, 107, (0, 0, 0))

wall2 = Rectangle(586, 0, 72, 114, (0, 0, 0))

wall3 = Rectangle(242, 600, 71, 107, (0, 0, 0))

wall4 = Rectangle(586, 600, 72, 114, (0, 0, 0))

wall5 = Rectangle(1, 240, 326, 54, (0, 0, 0))

Door = Rectangle(953, 182, 50, 160, (0, 0, 0))

button = GameSprite('big button.png', 727, 397, 50, 50, 0)

turrets = sprite.Group(turret3, turret4, turret5, turret6, turret7, turret8)

Cube = GameSprite('cube.png', 165, 61, 32, 32, 0)

Win_width = 1000
Win_height = 700
window = display.set_mode((Win_width, Win_height))
display.set_caption("Портал 2D")
display.set_icon(image.load("icon.png"))
clock = time.Clock()
FPS = 60
game = True
finish = False

screen = "menu"

players = sprite.Group()

players.add(player, lava, Door)

portal1 = sprite.GroupSingle()

portal2 = sprite.GroupSingle()

walls = sprite.Group()

walls.add(wall1, wall2, wall3, wall4)

bullets = sprite.Group()

menu = transform.scale(image.load("menu.png"), (1000, 700))

Howtoplay = transform.scale(image.load("Yakgraty.png"), (1000, 700))

minutes = 2
seconds = 0
interval = 1

bul_speed = 10

while game:
    clock.tick(FPS)
    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                screen = "menu"
    if screen == "menu":
        display.set_caption("Портал 2D - Menu")
        window.blit(menu, (0, 0))
        for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
                    x, y = e.pos
                    if 85 < x < 340 and 169 < y < 400:
                        screen = "game"
                    elif 679 < x < 907 and 425 < y < 697:
                        game = False
                    elif 671 < x < 956 and 173 < y < 380:
                        screen = "howtoplay"
                    elif 115 < x < 333 and 408 < y < 640:
                        if is_music == False:
                            mixer.music.play(-1)
                            is_music = True
                        else:
                            mixer.music.pause()
                            is_music = False
    elif screen == "howtoplay":
        display.set_caption("Портал 2D - How to play")
        window.blit(Howtoplay, (0, 0))
        for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
                    x, y = e.pos
                    if 660 < x < 926 and 15 < y < 281:
                        screen = "menu"
    elif finish == False and screen == "game":
        display.set_caption("Портал 2D - level " + str(level))

        window.fill(Color('white')) 
        player.update()
        player.reset()
        if level == 1:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
                    x, y = e.pos

                    port = True
                    for p in players:
                        if p.rect.collidepoint(x, y):
                            print(p)
                            port = False
                    if port == True:
                        print('Создаем портал')
                        if e.button == 1:
                            portal1.add( Portal('Portal1.png', x, y, 30, 40, 5))
                        elif e.button == 3:
                            portal2.add( Portal('Portal2.png', x, y, 30, 40, 5))  
            if player.rect.colliderect(lava.rect):
                player.rect.x = 75
                player.rect.y = 65
            if player.rect.colliderect(Door.rect):
                portal1.sprite.kill()
                portal2.sprite.kill()
                Door.isblocked = True
                level = 2
                player.rect.x = 75
                player.rect.y = 65
            if len(portal1) == 1 and len(portal2) == 1: 
                
                if player.rect.colliderect(portal1.sprite.rect): 
                    player.rect.x = portal2.sprite.rect.right + 5
                    player.rect.y = portal2.sprite.rect.y

                if player.rect.colliderect(portal2.sprite.rect): 
                    player.rect.right= portal1.sprite.rect.left - 5
                    player.rect.y = portal1.sprite.rect.y
        

            lava.reset()
            Door.reset()
            portal1.draw(window)
            portal2.draw(window)
        
        elif level == 2:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
            
            
            if player.rect.colliderect(Door.rect) and Door.isblocked == False:
                Door.isblocked = True
                level = 3
                player.rect.x = 75
                player.rect.y = 65
                Cube.rect.x = 165
                Cube.rect.y = 61
            if player.rect.colliderect(Cube.rect):
                player.cube = transform.scale(image.load('cube.png'), (32, 32))
            if Cube.rect.colliderect(button.rect):
                Door.isblocked = False
            if player.rect.colliderect(button.rect):
                player.cube = None
                Cube.rect.x = button.rect.x + 5
                Cube.rect.y = button.rect.y + 5
            button.reset()
            if player.cube == None:
            
                Cube.reset()
            Door.reset()

        elif level == 3:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
                    x, y = e.pos

                    port = True
                    for p in players:
                        if p.rect.collidepoint(x, y):
                            print(p)
                            port = False
                    if port == True:
                        print('Создаем портал')
                        if e.button == 1:
                            portal1.add( Portal('Portal1.png', x, y, 30, 40, 5))
                        elif e.button == 3:
                            portal2.add( Portal('Portal2.png', x, y, 30, 40, 5))
            
            if player.rect.colliderect(lava.rect):
                player.rect.x = 75
                player.rect.y = 65

            if len(portal1) == 1 and len(portal2) == 1: 
                
                if player.rect.colliderect(portal1.sprite.rect): 
                    player.rect.x = portal2.sprite.rect.right + 5
                    player.rect.y = portal2.sprite.rect.y

                if player.rect.colliderect(portal2.sprite.rect): 
                    player.rect.right= portal1.sprite.rect.left - 5
                    player.rect.y = portal1.sprite.rect.y    
            
            if player.rect.colliderect(Cube.rect):
                player.cube = transform.scale(image.load('cube.png'), (32, 32))
            if Cube.rect.colliderect(button.rect):
                Door.isblocked = False
            if player.rect.colliderect(button.rect):
                player.cube = None
                Cube.rect.x = button.rect.x + 5
                Cube.rect.y = button.rect.y + 5
            button.reset()
            if player.cube == None:
            
                Cube.reset()
            Door.reset()
            lava.reset()
            portal1.draw(window)
            portal2.draw(window)
            if player.rect.colliderect(Door.rect) and Door.isblocked == False:
                starttime = timers.time()
                portal1.sprite.kill()
                portal2.sprite.kill()
                players.empty()
                players.add(player, Door, turret, wall1, wall2)
                level = 4
                player.rect.x = 75
                player.rect.y = 65
        elif level == 4:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
                    x, y = e.pos
            turret.reset()
            turret2.reset()
            Door.reset()
            walls.draw(window)
            if player.rect.colliderect(Door.rect) and Door.isblocked == False:
                players.empty()
                bullets.empty()
                players.add(player, Door, wall5, turret3, turret4, turret5, turret6, turret7, turret8)
                level = 5
                Door = Rectangle(536, 191, 160, 140, (0,0,0))

                player.rect.x = 75
                player.rect.y = 65
            if player.rect.colliderect(turret.rect) or sprite.spritecollide(player, walls, False) or player.rect.colliderect(turret2.rect) or sprite.spritecollide(player, bullets, True):
                player.rect.x = 75
                player.rect.y = 65
            if (timers.time() - starttime) > 1:
                turret.shoot()
                turret2.shoot()
                starttime = timers.time()
            bullets.draw(window)
            bullets.update()
            sprite.groupcollide(walls, bullets, False, True)
        
        if level == 5:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
                    x, y = e.pos
                    port = True
                    for p in players:
                        if p.rect.collidepoint(x, y):
                            print(p)
                            port = False
                    if port == True:
                        print('Создаем портал')
                        if e.button == 1:
                            portal1.add( Portal('Portal1.png', x, y, 30, 40, 5))
                        elif e.button == 3:
                            portal2.add( Portal('Portal2.png', x, y, 30, 40, 5))
            if (timers.time() - starttime) > 1:
                for e in turrets:
                    e.shoot()
                starttime = timers.time()
            Door.reset()
            turrets.draw(window)
            wall5.reset()
            bullets.draw(window)
            bullets.update()
            portal1.draw(window)
            portal2.draw(window)
            if len(portal1) == 1 and len(portal2) == 1: 
                
                if player.rect.colliderect(portal1.sprite.rect): 
                    player.rect.x = portal2.sprite.rect.right + 5
                    player.rect.y = portal2.sprite.rect.y

                if player.rect.colliderect(portal2.sprite.rect): 
                    player.rect.right= portal1.sprite.rect.left - 5
                    player.rect.y = portal1.sprite.rect.y
            if player.rect.colliderect(Door.rect):
                startttime = timers.time()
                level = 6
                bullets.empty()
                player.rect.x = 553
                player.rect.y = 260
            if sprite.spritecollide(player, turrets, False) or sprite.collide_rect(player, wall5) or sprite.spritecollide(player, bullets, True):
                player.rect.x = 75
                player.rect.y = 65
        if level == 6:
            for e in events:
                if e.type == MOUSEBUTTONDOWN:
                    print(e.pos)
            GLaDOS.reset()
            if timers.time() - startttime >= 1:
                startttime = timers.time()
                if seconds == 0:
                    if minutes > 0:
                        if minutes == 1:
                            interval = 0.75
                            bul_speed = 15

                        minutes -= 1
                        seconds = 59
                    else:
                        screen = "win"
                else:
                    seconds -= 1
                if seconds == 30 and minutes == 0:
                    interval = 0.5
                    bul_speed = 20
            if sprite.spritecollide(player, bullets, True):
                player.rect.x = 75
                player.rect.y = 65
                minutes = 2
                seconds = 0
                interval = 1
                bul_speed = 10

            txt_time = font1.render(f'{minutes}:{seconds}', 1, (0, 0, 0))
                
            window.blit(txt_time, (5, 5))
            if (timers.time() - starttime) > interval:
                GLaDOS.shoot(bul_speed)
                starttime = timers.time()
            bullets.update()
            bullets.draw(window)
    if screen == "win":
            window.blit(transform.scale(image.load("Cake(or no).png"), (1000, 700)), (0, 0))
            display.set_caption("Портал 2D - Win")
    display.update()
    
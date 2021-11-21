import pygame
pygame.font.init()
sc = pygame.display.set_mode((1280, 720))
bg = pygame.image.load("BG5.png")
hero = pygame.image.load("hero.png")
x = 0
y = 0
x1 = 100
y1 = 200
hp = 100
color1 = 0
color2 = 255
speed = 4
f1 = pygame.font.Font(None, 36)
class world:
    def __init__():
        pass
    def control():
        global x
        global y
        global speed
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x -= speed
        elif keys[pygame.K_d]:
            x += speed
        elif keys[pygame.K_s]:
            y += speed
        elif keys[pygame.K_w]:
            y -= speed
    def locate():
        global bg
        global hero
        global x1
        global y1
        global hero_rect
        global mob_rect
        global strl1
        sc.blit(bg, (0, 0))
        sc.blit(hero, (x, y))
        sc.blit(hero, (x1, y1))
        hero_rect = pygame.Rect((x, y), (150, 150))
        mob_rect = pygame.Rect((x1, y1), (150, 150))

    def stlr():
        global hero_rect
        global mob_rect
        global strl1
        global hp
        global color1
        global color2
        global speed
        strl1 = hero_rect.colliderect(mob_rect)
        if strl1 == True:
            hp -= 0.03
            if hp <= 100 and hp > 30:
                color1 += 0.1
                color2 -= 0.1
    class player:
        def __init__(self):
            pass
        def hp1():
            global hp
            global text1
            global color1
            global color2
            text1 = f1.render(str(int(hp)), True,
                              (180, 0, 0))
            sc.blit(text1, (x, y))
            pygame.draw.rect(sc, (int(color1), int(color2), 0),
                             (20, 20, hp, 20))

while True:
    world.locate()
    world.player.hp1()
    world.control()
    world.stlr()
    pygame.display.flip()





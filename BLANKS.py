
import pygame
import sys

class game():
    def __init__(self):
        pygame.init()
        self.image_hero_1 = "../IMAGE_GAME/GHOST1.png"
        self.image_hero_2 = '../IMAGE_GAME/GHOST2.png'
        self.hero_red_2 = '../IMAGE_GAME/GHOST2_RED.png'
        self.hero_red_1 = '../IMAGE_GAME/GHOST1_RED.png'
        self.image_hero = pygame.image.load("../IMAGE_GAME/GHOST2.png")
        self.clock = pygame.time.Clock()
        self.edge_x = 60
        self.edge_y = 80
        self.size = self.w, self.h = (1000, 600)
        self.y_hero = self.h // 2
        self.x_hero = self.w // 2
        self.speed_hero = 20
        self.y_enemy = 70
        self.x_enemy = 70
        self.bg = pygame.image.load("../IMAGE_GAME/BG3.jpg")
        #self.screen = pygame.display.set_mode((self.size), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((self.size))
        while pygame.event.wait().type != pygame.QUIT:
            self.screen.blit(self.bg, (0, 0))
            self.draw()
            self.clock.tick(60)
            pygame.display.set_caption(f"FPS {self.clock.get_fps()}")
            pygame.display.update()
            pygame.display.flip()


    def draw(self):
        self.image_hero_sc = self.image_hero.get_rect(center=(self.x_hero, self.y_hero))
        self.screen.blit(self.image_hero, self.image_hero_sc)
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and keys[pygame.K_w] and self.y_hero > self.edge_y and self.x_hero > self.edge_x:
            self.x_hero -= self.speed_hero
            self.y_hero -= self.speed_hero
            if self.image_hero != pygame.image.load(self.image_hero_1):
                self.image_hero = pygame.image.load(self.image_hero_1)
        elif keys[pygame.K_a] and keys[pygame.K_s] and self.x_hero > self.edge_x and self.y_hero < self.h - self.edge_y:
            self.x_hero -= self.speed_hero
            self.y_hero += self.speed_hero
            if self.image_hero != pygame.image.load(self.image_hero_1):
                self.image_hero = pygame.image.load(self.image_hero_1)
        elif keys[pygame.K_d] and keys[pygame.K_s] and self.x_hero < self.w - self.edge_x and self.y_hero < self.h - self.edge_y:
            self.x_hero += self.speed_hero
            self.y_hero += self.speed_hero
            if self.image_hero != pygame.image.load(self.image_hero_2):
                self.image_hero = pygame.image.load(self.image_hero_2)
        elif keys[pygame.K_d] and keys[pygame.K_w] and self.y_hero > self.edge_y and self.x_hero < self.w - self.edge_x:
            self.x_hero += self.speed_hero
            self.y_hero -= self.speed_hero
            if self.image_hero != pygame.image.load(self.image_hero_2):
                self.image_hero = pygame.image.load(self.image_hero_2)

        elif keys[pygame.K_a] and self.x_hero > self.edge_x:
            self.x_hero -= self.speed_hero
            if self.image_hero != pygame.image.load(self.image_hero_1):
                self.image_hero = pygame.image.load(self.image_hero_1)
        elif keys[pygame.K_d] and self.x_hero < self.w - self.edge_x:
            self.x_hero += self.speed_hero
            if self.image_hero != pygame.image.load(self.image_hero_2):
                self.image_hero = pygame.image.load(self.image_hero_2)
        elif keys[pygame.K_w] and self.y_hero > self.edge_y:
            self.y_hero -= self.speed_hero
        elif keys[pygame.K_s] and self.y_hero < self.h - self.edge_y:
            self.y_hero += self.speed_hero
        if keys[pygame.K_SPACE] and self.image_hero == pygame.image.load(self.image_hero_2):
            self.image_hero_2 = pygame.image.load(self.hero_red_2)
        elif keys[pygame.K_SPACE] and self.image_hero == pygame.image.load(self.image_hero_2):
            self.image_hero_1 = pygame.image.load(self.hero_red_1)


if __name__ == '__main__':
    a = game()
    pygame.quit()
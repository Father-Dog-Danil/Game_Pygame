import pygame
import sys

class game():
    def __init__(self):
        pygame.init()
        self.image_hero_0 = pygame.image.load('../IMAGE_GAME/DOWN_KEN.png')
        self.image_hero_1 = pygame.image.load('../IMAGE_GAME/L_REV_KEN.png')
        self.image_hero_2 = pygame.image.load('../IMAGE_GAME/R_REV_KEN.png')
        self.image_hero_3 = pygame.image.load('../IMAGE_GAME/BACK_REV_KEN.png')

        self.list_anime_right = [
            pygame.image.load('../IMAGE_GAME/R_REV_KEN.png'), pygame.image.load('../IMAGE_GAME/R_REV_KEN1.png'),
            pygame.image.load('../IMAGE_GAME/R_REV_KEN.png'), pygame.image.load('../IMAGE_GAME/R_REV_KEN2.png'),
            pygame.image.load('../IMAGE_GAME/R_REV_KEN.png')]

        self.list_anime_left = [
            pygame.image.load('../IMAGE_GAME/L_REV_KEN.png'), pygame.image.load('../IMAGE_GAME/L_REV_KEN1.png'),
            pygame.image.load('../IMAGE_GAME/L_REV_KEN.png'), pygame.image.load('../IMAGE_GAME/L_REV_KEN2.png'),
            pygame.image.load('../IMAGE_GAME/L_REV_KEN.png')]

        self.list_anime_up = [
            pygame.image.load('../IMAGE_GAME/BACK_REV_KEN.png'), pygame.image.load('../IMAGE_GAME/BACK_REV_KEN1.png'),
            pygame.image.load('../IMAGE_GAME/BACK_REV_KEN.png'), pygame.image.load('../IMAGE_GAME/BACK_REV_KEN2.png'),
            pygame.image.load('../IMAGE_GAME/BACK_REV_KEN.png')]

        self.list_anime_down = [
            pygame.image.load('../IMAGE_GAME/DOWN_KEN.png'), pygame.image.load('../IMAGE_GAME/DOWN_KEN1.png'),
            pygame.image.load('../IMAGE_GAME/DOWN_KEN.png'), pygame.image.load('../IMAGE_GAME/DOWN_KEN2.png'),
            pygame.image.load('../IMAGE_GAME/DOWN_KEN.png')]
        self.image_hero = (self.image_hero_0)
        self.clock = pygame.time.Clock()
        self.count = 0
        self.edge_x = 60
        self.edge_y = 80
        self.size = self.w, self.h = (1280, 720)
        self.y_hero = self.h // 2
        self.x_hero = self.w // 2
        self.speed_hero = 10
        self.y_enemy = 70
        self.x_enemy = 70
        self.bg = pygame.image.load("../IMAGE_GAME/BG5.png")
        self.screen = pygame.display.set_mode((self.size), pygame.FULLSCREEN)
        while pygame.event.wait().type != pygame.QUIT:
            self.screen.blit(self.bg, (0, 0))
            self.draw()
            self.clock.tick(60)
            pygame.display.update()
            pygame.display.flip()


    def draw(self):
        self.hero_coordinate = self.image_hero.get_rect(center=(self.x_hero, self.y_hero))
        self.screen.blit(self.image_hero, self.hero_coordinate)
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and keys[pygame.K_w] and self.y_hero > self.edge_y and self.x_hero > self.edge_x:
            self.x_hero -= self.speed_hero
            self.y_hero -= self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_left[self.count // 2]
            self.count += 1
        elif keys[pygame.K_a] and keys[pygame.K_s] and self.x_hero > self.edge_x and self.y_hero < self.h - self.edge_y:
            self.x_hero -= self.speed_hero
            self.y_hero += self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_left[self.count // 2]
            self.count += 1
        elif keys[pygame.K_d] and keys[pygame.K_s] and self.x_hero < self.w - self.edge_x and self.y_hero < self.h - self.edge_y:
            self.x_hero += self.speed_hero
            self.y_hero += self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_right[self.count // 2]
            self.count += 1
        elif keys[pygame.K_d] and keys[pygame.K_w] and self.y_hero > self.edge_y and self.x_hero < self.w - self.edge_x:
            self.x_hero += self.speed_hero
            self.y_hero -= self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_right[self.count // 2]
            self.count += 1

        elif keys[pygame.K_a] and self.x_hero > self.edge_x:
            self.x_hero -= self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_left[self.count // 2]
            self.count += 1
        elif keys[pygame.K_d] and self.x_hero < self.w - self.edge_x:
            self.x_hero += self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_right[self.count // 2]
            self.count += 1

        elif keys[pygame.K_w] and self.y_hero > self.edge_y:
            self.y_hero -= self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_up[self.count // 2]
            self.count += 1

        elif keys[pygame.K_s] and self.y_hero < self.h - self.edge_y:
            self.y_hero += self.speed_hero
            if self.count + 1 >= 10:
                self.count = 0
            self.image_hero = self.list_anime_down[self.count // 2]
            self.count += 1


if __name__ == '__main__':
    a = game()
    pygame.quit()

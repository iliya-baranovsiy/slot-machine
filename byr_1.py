import pygame
import sys
from button import Button
import random
from random import randint
import time


class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Monocraft', 50)
        self.screen = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Byrmalda")
        self.bg_img = pygame.image.load("photos/phone.jpg")
        self.back = pygame.transform.scale(self.bg_img, (800, 700))
        # self.screen.blit(self.back, (0, 0))
        self.clock = pygame.time.Clock()
        self.FPS = 90
        self.default_score = 100
        self.start_ = None
        self.win_out = 0
        self.n = 0

        self.rand = randint(35, 45)

        self.im_list_1 = [pygame.image.load("photos/cherry.png"), pygame.image.load("photos/banana.png"),
                          pygame.image.load("photos/grape.png")]

        self.rand_1 = 0
        self.rand_2 = 1
        self.rand_3 = 2

    def anim(self):
        for i in range(self.rand + 2):
            self.rand_1 = random.randint(0, 2)
            self.rand_2 = random.randint(0, 2)
            self.rand_3 = random.randint(0, 2)

            self.screen.blit(self.im_list_1[self.rand_1], (135, 290))
            self.screen.blit(self.im_list_1[self.rand_2], (323, 290))
            self.screen.blit(self.im_list_1[self.rand_3], (510, 290))

            pygame.display.update()
            i += 1
            time.sleep(0.09)

    def spin(self):
        self.start_ = True
        self.default_score = self.default_score - 5
        self.n = 0

    def start(self):
        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if self.default_score < 0:
                break

            self.but = Button(425, 490, 180, 50, 'Spin', self.screen, self.spin)
            self.but.run()

            self.text_win = f'Win:  {str(self.win_out)}'
            self.txt = self.my_font.render(self.text_win, False, (255, 255, 255))
            self.screen.blit(self.txt, (375, 40))

            self.text = f"Money:  {self.default_score} $"
            self.txt = self.my_font.render(self.text, False, (255, 255, 255))
            self.screen.blit(self.txt, (35, 40))

            self.text = "1 spin = 5 $"
            self.txt = self.my_font.render(self.text, False, (255, 255, 255))
            self.screen.blit(self.txt, (590, 40))

            pygame.display.update()

            if self.start_ == True:
                pygame.display.update()
                self.anim()
            self.start_ = False

            self.screen.blit(self.im_list_1[self.rand_1], (135, 290))
            self.screen.blit(self.im_list_1[self.rand_2], (323, 290))
            self.screen.blit(self.im_list_1[self.rand_3], (510, 290))

            if self.n == 0:
                if self.rand_1 == self.rand_2 == self.rand_3:
                    self.win_out = 100
                    self.default_score += self.win_out
                elif self.rand_1 == self.rand_2:
                    self.win_out = 25
                    self.default_score += self.win_out
                elif self.rand_2 == self.rand_3:
                    self.win_out = 10
                    self.default_score += self.win_out
                else:
                    self.win_out = 0

            pygame.display.update()
            pygame.display.flip()
            self.n = 1
            self.screen.blit(self.back, (0, 0))


if __name__ == '__main__':
    by = Game()
    by.start()

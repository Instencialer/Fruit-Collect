import pygame, sys, random
from external import decor, apples, label, bombs
from pygame.locals import *
pygame.init()

pygame.display.set_caption("FruitCollect")
decoration = decor()

class game():
    def __init__(self):
        self.WINDOW_SIZE = (500, 700)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)
        self.clock = pygame.time.Clock()    
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)
        self.capy = pygame.transform.scale(pygame.image.load("IMG/sprite1.png"), (64, 64))
        self.capypos = 0
        self.movingright = False
        self.movingleft = False
        self.score = 0
        self.fruits = []
        self.frame = 0
        self.speed = 3
        self.mode = "PLAYING"
        self.highscore = 0
        self.button = pygame.image.load("IMG/button.png")
        self.buttonrect = self.button.get_rect()
        self.buttonrect.center = (250, 450)
        self.button2 = pygame.image.load("IMG/button2.png")
        self.button2rect = self.button2.get_rect()
        self.button2rect.center = (250, 450)

    def calc(self):
        extra = int(self.score / 25)
        self.speed = min((3+extra), 8)
        if (self.movingright):
            if (self.capypos < 436):
                self.capypos += 5
        if (self.movingleft):
            if (self.capypos > 0):
                self.capypos -= 5
        self.frame += 1
        if (self.frame == 20):
            self.frame = 0
            val = random.randint(1, 100)
            if (val <= min(int(self.score)+1, 95)):
                bomb = bombs()
                self.fruits.append(bomb)
            else:
                apple = apples()
                self.fruits.append(apple)
        x = 0
        for item in self.fruits:
            check = item.calc(self.capypos, self.speed)
            if (check == "POINTS"):
                self.score += 1
                self.fruits.pop(x)
            elif (check == "OOFED"):
                print("YOU LOSE")
                self.mode = "GAMEOVER"
            if (item.y > 700):
                self.fruits.pop(x)
            x += 1    

    def gui(self):
        for item in self.fruits:
            self.screen.blit(item.img, (item.x, item.y))
        scoretext = label(f"SCORE: {self.score}", 18)
        self.screen.blit(scoretext, (10,10))

    def render(self, clicked):
        self.screen.fill((135, 206, 235))
        land = pygame.Rect((0, 550, 500, 150))
        pygame.draw.rect(self.screen, (118, 197, 120), land)
        pygame.draw.line(self.screen, (0,0,0), (0, 549), (500, 549), width=2)
        decoration.rendering(self.screen)
        self.screen.blit(self.capy, (self.capypos, 520))
        self.gui()  
        if (self.mode == "GAMEOVER"):
            text = label("GAMEOVER", 48)
            textrect = text.get_rect()
            textrect.center = (250, 250)
            self.screen.blit(text, textrect)
            if (self.score > self.highscore):
                self.highscore = self.score
            text2 = label(f"HIGH SCORE : {self.highscore}", 20)
            text2rect = text2.get_rect()
            text2rect.center = (250, 310)
            self.screen.blit(text2, text2rect)
            x, y = pygame.mouse.get_pos()
            mouserect = pygame.Rect(x, y, 1, 1)
            if self.buttonrect.colliderect(mouserect):
                self.screen.blit(self.button2, self.buttonrect)
                if clicked:
                    return True
            else:
                self.screen.blit(self.button, self.buttonrect)
        pygame.display.update()


    def restrat(self):
        self.score = 0
        self.capypos = 0
        self.frame = 0
        self.fruits.clear()
        self.mode = "PLAYING"

thegame = game()

while True:

    clicked = False
    check = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if ((event.key == K_a) or (event.key == K_LEFT)):
                thegame.movingleft = True
            if ((event.key == K_d) or (event.key == K_RIGHT)):
                thegame.movingright = True
        if event.type == KEYUP:
            if ((event.key == K_a) or (event.key == K_LEFT)):
                thegame.movingleft = False
            if ((event.key == K_d) or (event.key == K_RIGHT)):
                thegame.movingright = False
        if event.type == MOUSEBUTTONDOWN:
            clicked = True

    if (thegame.mode == "PLAYING"):
        thegame.calc()
    check = thegame.render(clicked)
    if check:
        thegame.restrat()
    thegame.clock.tick(60)

    
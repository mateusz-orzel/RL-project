import pygame

class Snake:
    def __init__ (self, x, y, speed = 5) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.color = (10, 10, 100)
        self.g = 1

    def collide(self, ?):
        pass
        
    def draw(self, win):
        self.y += self.g
        pygame.draw.(self.x, self.y, self.color)
        
    def move(self):
        pass

class 

class Game:
    def __init__(self) -> None:
        self.window = pygame.display.set_mode((1200, 700))
        self.score = 0
        def main(self):
            run = True
            snake = Snake(90, 150)

            while run:
                self.window.fill((255, 255, 255))

                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        run = False
                        pygame.quit()
                        quit()
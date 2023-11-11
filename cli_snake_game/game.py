## game.py
import pygame
import time
from snake import Snake
from food import Food

class Game:
    def __init__(self, screen_size: tuple = (800, 600)):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.score = 0
        self.game_over = False
        self.snake = Snake()
        self.food = Food()

    def render_score(self):
        font = pygame.font.Font(None, 36)
        text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() - text.get_width() - 10, 10))
        self.screen = pygame.display.set_mode(self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.score = 0
        self.game_over = False
        self.snake = Snake()
        self.food = Food()

    def start_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = "UP"
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = "DOWN"
                    elif event.key == pygame.K_LEFT:
                        self.snake.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = "RIGHT"
            self.snake.move()
            if self.snake.check_collision():
                self.game_over = True
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food.generate()
            self.update_display()
            time.sleep(0.1)

    def end_game(self):
        pygame.quit()

    def update_display(self):
        self.screen.fill((0, 0, 0))
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(segment[0], segment[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], 10, 10))
        self.render_score()
        pygame.display.flip()

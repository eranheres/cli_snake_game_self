## game.py
import time

import pygame

from cli_snake_game.food import Food
from cli_snake_game.snake import Snake


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
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (self.screen.get_width() - text.get_width() - 10, 10))

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
            if self.snake.move():
                self.game_over = True
            elif self.snake.check_collision():
                self.game_over = True
            elif self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food.generate()
            self.update_display()
            time.sleep(0.1)

    def end_game(self):
        pygame.quit()

    def update_display(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(
            self.screen, (255, 255, 255), pygame.Rect(0, 0, self.screen.get_width(), 10)
        )  # Top border
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(0, 0, 10, self.screen.get_height()),
        )  # Left border
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(0, self.screen.get_height() - 10, self.screen.get_width(), 10),
        )  # Bottom border
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            pygame.Rect(self.screen.get_width() - 10, 0, 10, self.screen.get_height()),
        )  # Right border
        for segment in self.snake.body:
            if segment == self.snake.body[0]:
                pygame.draw.rect(
                    self.screen,
                    (144, 238, 144),
                    pygame.Rect(segment[0], segment[1], 10, 10),
                )
            else:
                pygame.draw.rect(
                    self.screen,
                    (0, 255, 0),
                    pygame.Rect(segment[0], segment[1], 10, 10),
                )
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(self.food.position[0], self.food.position[1], 10, 10),
        )
        self.render_score()
        pygame.display.flip()

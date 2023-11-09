## food.py
import random

class Food:
    def __init__(self, position: tuple = (100, 100)):
        self.position = position

    def generate(self):
        self.position = (random.randint(0, 79) * 10, random.randint(0, 59) * 10)

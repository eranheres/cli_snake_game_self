import secrets

from colorama import Fore, Style


class Snake:
    def __init__(self, initial_body: list = None, initial_direction: str = "RIGHT"):
        if initial_body is None:
            initial_body = [(40, 40), (30, 40), (20, 40)]
        self.body = initial_body
        self.direction = initial_direction

    def move(self):
        head = self.body[0]
        move_directions = {
            "UP": (head[0], head[1] - 10),
            "DOWN": (head[0], head[1] + 10),
            "LEFT": (head[0] - 10, head[1]),
            "RIGHT": (head[0] + 10, head[1]),
        }
        print(self.color)
        new_head = move_directions.get(self.direction)
        self.body.insert(0, new_head)
        print(Style.RESET_ALL)
        self.body.pop()

        # Check if the snake has hit the border
        if new_head[0] < 0 or new_head[0] > 790 or new_head[1] < 0 or new_head[1] > 590:
            return True
        else:
            return False

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        return self.body[0] in self.body[1:]


class Food:
    def __init__(self, position: tuple = (100, 100)):
        self.position = position

    def generate(self):
        self.position = (secrets.randbelow(80) * 10, secrets.randbelow(60) * 10)
        self.color = Fore.LIGHTGREEN_EX

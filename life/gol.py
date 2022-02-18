from sys import exit
from typing import List

import pygame


class Cell:
    def __init__(self, is_alive: bool = False):
        self.is_alive: bool = is_alive
        self._next_state: bool = False

    def die(self) -> None:
        self._next_state = False

    def reproduce(self) -> None:
        self._next_state = True

    def update(self) -> None:
        self.is_alive = self._next_state


class Game:
    def __init__(self, width: int, height: int, block_size: int):
        pygame.init()
        self.BLACK = 0, 0, 0
        self.GREEN = 0, 255, 0
        self.AOC_PURPLE = 110, 70, 139
        self.AOC_OCEAN = 20, 178, 173
        self._horizontal_block_count = width
        self._vertical_block_count = height
        self._block_size = block_size
        self._width = width * self._block_size
        self._height = height * self._block_size
        self._size = self._width, self._height
        self._screen = self.setup_screen()
        self._cells: List[List[Cell]] = self.create_grid()
        self.x_coordinate_range = range(0, self._horizontal_block_count - 1)
        self.y_coordinate_range = range(0, self._vertical_block_count - 1)

    def setup_screen(self):
        screen = pygame.display.set_mode(size=self._size)
        screen.fill(self.BLACK)
        return screen

    def create_grid(self) -> List[List[Cell]]:
        return [[Cell() for y in range(0, self._vertical_block_count)] for x in range(0, self._horizontal_block_count)]

    def set_initial_state(self, alive_cells) -> None:
        for alive_cell_x, alive_cell_y in alive_cells:
            self._cells[alive_cell_x][alive_cell_y].reproduce()

    def draw_grid(self) -> None:
        self._screen.fill(self.BLACK)
        [
            [
                pygame.draw.rect(self._screen, self.GREEN, self.make_cell(x, y))
                for x in self.x_coordinate_range
                if self._cells[x][y].is_alive
            ]
            for y in self.y_coordinate_range
        ]

    def make_cell(self, x, y):
        return pygame.Rect(x * self._block_size, y * self._block_size, self._block_size, self._block_size)

    def get_neighbour_coordinates(self, x, y) -> List[tuple[int, int]]:
        coordinates = [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]
        return [
            (x, y)
            for (x, y) in coordinates
            if 0 <= x < self._horizontal_block_count and 0 <= y < self._vertical_block_count
        ]

    def get_neighbours_alive_count(self, x, y) -> int:
        return sum([1 if self._cells[x][y].is_alive is True else 0 for (x, y) in self.get_neighbour_coordinates(x, y)])

    def update_cell_state(self) -> None:
        [[self._cells[x][y].update() for x in self.x_coordinate_range] for y in self.y_coordinate_range]

    def evaluate_cells(self) -> None:
        [[self.logic(x, y) for x in self.x_coordinate_range] for y in self.y_coordinate_range]

    def logic(self, x, y) -> None:
        neighbours_alive_count = self.get_neighbours_alive_count(x, y)
        if self._cells[x][y].is_alive:
            if neighbours_alive_count < 2 or neighbours_alive_count > 3:
                self._cells[x][y].die()
        else:
            if neighbours_alive_count == 3:
                self._cells[x][y].reproduce()

    def game_loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.draw_grid()
            pygame.display.update()
            self.evaluate_cells()
            self.update_cell_state()


if __name__ == "__main__":
    game = Game(width=160, height=120, block_size=6)
    game.set_initial_state(
        [
            (12, 6),
            (12, 7),
            (13, 6),
            (13, 7),
            (22, 6),
            (22, 7),
            (22, 8),
            (23, 5),
            (23, 9),
            (24, 4),
            (24, 10),
            (25, 4),
            (25, 10),
            (26, 7),
            (27, 5),
            (27, 9),
            (28, 6),
            (28, 7),
            (28, 8),
            (29, 7),
            (32, 4),
            (32, 5),
            (32, 6),
            (33, 4),
            (33, 5),
            (33, 6),
            (34, 3),
            (34, 7),
            (36, 2),
            (36, 3),
            (36, 7),
            (36, 8),
            (46, 4),
            (46, 5),
            (47, 4),
            (47, 5),
        ]
    )
    game.game_loop()

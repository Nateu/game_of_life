# Python Kata - Game of Life

For this kata I set up a couple of starting points:

* Python 3.10.0
* Poetry
* Makefile
* Flake8, Black, iSort
* Mamba test runner
* pygame support through a Graphics class (see below)
* A Game class with
  * Constructor for setting up the initial things like game screen size, dependency injection etc.
  * A method init_screen for actually hooking up pygame
  * A method game_loop where the logic should go

## Logic rules
Game of life basic logic
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation. 
3. Any live cell with more than three live neighbours dies, as if by overpopulation. 
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

[Wikipedia article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Principles
Stick to these principles a much as possible:

* Red = Failing test, Green = working implementation, Refactor; both implementation and tests!
* Work in small steps
* Don't build anything you don't need
* Only move to the next task when you're done refactoring
* Over time: Tests become more specific, code becomes more general
* Don't mock what you don't own, hence the delegate

## Your task list
Follow this task list.

1. Create a game of life simulator with exactly one live cell
2. Create a game of life with two non-neighbouring live cells
3. Create a game of life with two neighbouring live cells
4. Create a game of life with 4 neighbouring live cells
5. Create a game of life with 3 non-neighbouring live cells that have a shared neighbour cell
6. Create a way to load a list of initial alive cell x,y coordinates (see Initial state for the game)
7. Create a main.py to launch an actual game with pygame to see if it all works
8. Optimize by tracking only alive cells and their neighbours

### Initial state for the game
This will be used in step 6
![should look like this](Gospers_glider_gun.gif)  
It should result in something like this
```python
initial_state = [(12, 6),(12, 7),
(13, 6),(13, 7),
(22, 6),(22, 7),(22, 8),
(23, 5),(23, 9),
(24, 4),(24, 10),
(25, 4),(25, 10),
(26, 7),
(27, 5),(27, 9),
(28, 6),(28, 7),(28, 8),
(29, 7),
(32, 4),(32, 5),(32, 6),
(33, 4),(33, 5),(33, 6),
(34, 3),(34, 7),
(36, 2),(36, 3),(36, 7),(36, 8),
(46, 4),(46, 5),
(47, 4),(47, 5)]
```


### Basic pygame code wrapped in the Graphics class
This is all you will need to get started. Make sure you keep all pygame related code in this delegate.

``` python
import pygame


class Graphics:
    def __init__(self):
        pygame.init()
        self.screen = None

    def init_screen(self, size: tuple[int, int]) -> None:
        self.screen = pygame.display.set_mode(size=size)

    def fill_screen(self, colour: tuple[int, int, int]) -> None:
        if self.screen:
            self.screen.fill(colour)

    def draw_cell(self, x: int, y: int, width: int, height: int, colour: tuple[int, int, int]) -> None:
        rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, colour, rect)

    def update(self) -> None:
        pygame.display.update()

    def has_quit(self) -> bool:
        result: bool = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                result = True
        return result
```

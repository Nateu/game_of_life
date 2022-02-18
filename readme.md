


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
        pygame.display.update()

    def has_quit(self) -> bool:
        result: bool = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                result = True
        return result
```



Initial state:
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

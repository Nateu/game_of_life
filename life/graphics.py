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

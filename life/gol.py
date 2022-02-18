from life.graphics import Graphics


class Game:
    def __init__(self, graphics: Graphics, size: tuple[int, int], my_exit: callable):
        self.BLACK = 0, 0, 0
        self.GREEN = 0, 255, 0
        self.graphics = graphics
        self.graphics.init_screen(size=size)
        self.stop = False
        self.exit = my_exit

    def setup_screen(self):
        self.graphics.fill_screen(self.BLACK)

    def game_loop(self) -> None:
        while not self.stop:
            if self.graphics.has_quit():
                self.exit()
                self.stop = True

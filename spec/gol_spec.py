import sys
from unittest.mock import MagicMock

from mamba import _context, before, context, description, it

from life.gol import Game
from life.graphics import Graphics


class FakeGraphics(Graphics):
    def init_screen(self, size: tuple[int, int]) -> None:
        pass

    def fill_screen(self, colour: tuple[int, int, int]) -> None:
        pass

    def draw_cell(self, x: int, y: int, width: int, height: int, colour: tuple[int, int, int]) -> None:
        pass

    def update(self) -> None:
        pass

    def has_quit(self) -> bool:
        pass


with description("Given a new game") as self:
    with context("when created with a specific size"):
        with before.each:
            self.fake_graphics = FakeGraphics()
            self.fake_graphics.init_screen = MagicMock(return_value=None)
            self.fake_graphics.fill_screen = MagicMock(return_value=None)
            self.fake_graphics.has_quit = MagicMock(return_value=True)
            self.my_exit = MagicMock(return_value=None)
            self.game = Game(graphics=self.fake_graphics, size=(100, 100), my_exit=self.my_exit)

        with it("should have a canvas with the right size"):
            self.fake_graphics.init_screen.assert_called_once_with(size=(100, 100))

        with context("and the screen is set up"):
            with it("should be filled with RGB 0 0 0"):
                self.game.setup_screen()
                self.fake_graphics.fill_screen.assert_called_once_with((0, 0, 0))

        with context("and the game has not quit"):
            with it("should keep going"):
                self.game.game_loop()
                self.my_exit.assert_called_once_with()

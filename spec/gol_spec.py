from expects import equal, expect
from mamba import context, description, it

from life.gol import Game
from life.graphics import Graphics


class FakeGraphics(Graphics):
    def init_screen(self, size: tuple[int, int]) -> None:
        pass

    def fill_screen(self, colour: tuple[int, int, int]) -> None:
        pass

    def draw_cell(self, x: int, y: int, width: int, height: int, colour: tuple[int, int, int]) -> None:
        pass

    def has_quit(self) -> bool:
        pass


with description("Given a new game") as self:
    with context("when created"):
        with it("should have a black canvas"):
            game = Game(graphics=FakeGraphics(), size=(100, 100))

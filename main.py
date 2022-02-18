class Bit:
    def __init__(self, id: str):
        self.id = id


x_range = range(0, 10)
y_range = range(0, 5)
loop = [[Bit(f"{x}, {y}") for y in y_range] for x in x_range]

for x in range(0, 9):
    for y in range(0, 4):
        print(loop[x][y].id)

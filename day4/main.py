import itertools


def main(file_name: str, part: int):
    with open(file_name) as f:
        grid = f.read().split()
        grid = list(map(list, grid))

    max_y, max_x = len(grid), len(grid[0])
    good_rolls = []

    def is_good_roll(y: int, x: int):
        if grid[y][x] != "@":
            return False

        n_rolls = 0
        for i, j in itertools.product(range(max(0, y-1), min(max_y, y+2)),
                                      range(max(0, x-1), min(max_x, x+2))):
            if i == y and j == x:
                continue
            if grid[i][j] == "@":
                n_rolls += 1

            if n_rolls >= 4:
                return False
        return True

    while True:
        n_old_rolls = len(good_rolls)
        for y, x in itertools.product(range(max_y), range(max_x)):
            if is_good_roll(y, x):
                good_rolls.append((y, x))

        if len(good_rolls) == n_old_rolls:
            break

        for y, x in good_rolls:
            grid[y][x] = "x"

        if part == 1:
            break

    print(len(good_rolls))


if __name__ == "__main__":
    main("input2.txt", part=1)
    main("input2.txt", part=2)



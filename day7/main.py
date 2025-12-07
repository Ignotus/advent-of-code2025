import pprint
from collections import deque

def split_count(pos_S: int, data: list[list[str]]) -> int:
    c = 0
    beam_positions = [pos_S]
    for i in range(1, len(data)):
        new_positions = []
        for pos in set(beam_positions):
            match data[i][pos]:
                case  ".":
                    new_positions.append(pos)
                case "^":
                    c += 1
                    new_positions.append(pos - 1)
                    new_positions.append(pos + 1)
        beam_positions = new_positions

    return c


def timeline_count(pos_S: int, data: list[list[str]]) -> int:
    """ An optimized version with a bit of dynamic programming."""
    c_map = [[0 for _ in row] for row in data]
    c_map[0][pos_S] = 1

    num_row = len(data)
    num_col = len(data[0])
    for i in range(1, num_row):
        for j in range(num_col):
            if data[i][j] == ".":
                c_map[i][j] += c_map[i-1][j]
            elif data[i][j] == "^":
                if j > 0:
                    c_map[i][j-1] += c_map[i-1][j]
                if j < num_col - 1:
                    c_map[i][j+1] += c_map[i-1][j]

    c = sum(c_map[-1])

    return c

def timeline_count_v2(pos_S: int, data: list[list[str]]) -> int:
    """ DFS implementation. Too slow. """
    c = 0

    num_row = len(data)
    stack = deque()
    stack.append((1, pos_S))

    while stack:
        row, pos = stack.pop()

        if row == num_row:
            c += 1
            print(c)
            continue

        match data[row][pos]:
            case ".":
                stack.append((row + 1, pos))
            case "^":
                stack.append((row + 1, pos - 1))
                stack.append((row + 1, pos + 1))

    return c


def main(file_name: str):
    with open(file_name) as f:
        data = [list(l[:-1]) for l in f]

    pos_S = data[0].index("S")
    # print(split_count(pos_S, data))
    print(timeline_count(pos_S, data))


if __name__ == "__main__":
    main("input2.txt")

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


def main(file_name: str):
    with open(file_name) as f:
        data = [list(l[:-1]) for l in f]

    pos_S = data[0].index("S")
    print(split_count(pos_S, data))


if __name__ == "__main__":
    main("input1.txt")

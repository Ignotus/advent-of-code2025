Point = tuple[int, int]

def area(p1: Point, p2: Point) -> int:
    return (abs(p2[1] - p1[1]) + 1) * (abs(p2[0] - p1[0]) + 1)


def part1(file_name: str):
    with open(file_name) as f:
        data = [list(map(int, l.split(","))) for l in f]

    max_area = max(
        area(p1, data[j])
        for i, p1 in enumerate(data)
        for j in range(i + 1, len(data))
    )

    print(max_area)


def contains(
    p: Point,
    border: list[tuple[Point, Point]]
) -> bool:
    for p1, p2 in border:
        if p1[0] == p2[0] == p[0]:
            if min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1]):
                return True

        if p1[1] == p2[1] == p[1]:
            if min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0]):
                return True

    c = 0
    for p1, p2 in border:
        if p1[1] == p2[1]:
            continue

        if p1[1] > p2[1]:
            p1, p2 = p2, p1

        if p1[1] <= p[1] < p2[1]:
            if p1[0] > p[0]:
                c += 1

    return c % 2 == 1


def intersects_border(
    box: tuple[Point, Point],
    border: list[tuple[Point, Point]]
) -> bool:
    p1, p2 = box
    for l1, l2 in border:
        box1_xmax = max(l1[0], l2[0])
        box2_xmin = min(p1[0], p2[0])

        box1_xmin = min(l1[0], l2[0])
        box2_xmax = max(p1[0], p2[0])
        if (box1_xmax <= box2_xmin) or (box1_xmin >= box2_xmax):
            continue

        box1_ymax = max(l1[1], l2[1])
        box2_ymin = min(p1[1], p2[1])

        box1_ymin = min(l1[1], l2[1])
        box2_ymax = max(p1[1], p2[1])
        if (box1_ymax <= box2_ymin) or (box1_ymin >= box2_ymax):
            continue

        return True

    return False


def part2(file_name: str):
    with open(file_name) as f:
        data = [list(map(int, l.split(","))) for l in f]

    border = list(zip(data, data[1:] + [data[0]]))

    max_area = max(
        area(p1, data[j])
        for i, p1 in enumerate(data)
        for j in range(i + 1, len(data))
        if (
            contains([p1[0], data[j][1]], border)
            and contains([data[j][0], p1[1]], border)
            and not intersects_border([p1, data[j]], border)
        )
    )

    print(max_area)


if __name__ == "__main__":
    part1("input1.txt")
    part1("input2.txt")

    part2("input1.txt")
    part2("input2.txt")

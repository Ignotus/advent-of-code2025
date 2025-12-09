import itertools

def area(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(y2 - y1) + 1) * (abs(x2 - x1) + 1)

def main(file_name: str):
    with open(file_name) as f:
        data = [list(map(int, l.split(","))) for l in f]

    max_area = max(
        area(x1, y1, x2, y2)
        for (x1, y1), (x2, y2) in itertools.combinations_with_replacement(data, r=2)
    )

    print(max_area)

if __name__ == "__main__":
    main("input1.txt")
    main("input2.txt")

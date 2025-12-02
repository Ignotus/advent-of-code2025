from typing import Callable

def is_invalid1(num: str) -> bool:
    if len(num) % 2:
        return False

    return num[:len(num) // 2] == num[len(num) // 2:]


def main(file_name: str, is_invalid: Callable[[str], bool]) -> None:
    with open(file_name) as f:
        ranges = [
            map(int, l.split("-", 1))
            for l in next(f).split(",")
        ]

        res = 0
        for s, e in ranges:
            for num in range(s, e + 1):
                num_s = str(num)
                if is_invalid(num_s):
                    res += num
        print(res)


def is_invalid2(num: str) -> bool:
    for d in range(2, len(num) + 1):
        if len(num) % d:
            continue

        chunk_size = len(num) // d
        chunks = [
            num[i * chunk_size: (i + 1) * chunk_size]
            for i in range(d)
        ]

        if all([chunk1 == chunk2 for chunk1, chunk2 in zip(chunks, chunks[1:])]):
            return True

    return False


if __name__ == "__main__":
    main("input.txt", is_invalid1)
    main("input.txt", is_invalid2)

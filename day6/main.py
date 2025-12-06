import functools
import operator
import numpy as np

def compute(op: str, args: list[str]):
    op = operator.add if op == "+" else operator.mul
    return functools.reduce(op, map(int, args))


def part1(file_name: str):
    with open(file_name) as f:
        data = [l.split() for l in f]
        data = data[-1:] + data[:-1]

    s = 0
    for op, *args in zip(*data):
        s += compute(op, args)
    print(s)


def group(nums: list[str]):
    grouped_nums = []
    group = []
    for n in nums:
        if n:
            group.append(n)
        else:
            grouped_nums.append(group)
            group = []
    if group:
        grouped_nums.append(group)

    return grouped_nums


def part2(file_name: str):
    with open(file_name) as f:
        data = np.asarray([list(l[:-1]) for l in f])

    ops = "".join(data[-1]).split()
    nums = data[:-1].T.tolist()
    nums = list(map(lambda x: "".join(x).strip(), nums))

    s = 0
    for op, n in zip(ops, group(nums)):
        s += compute(op, n)
    print(s)


if __name__ == "__main__":
    part1("input2.txt")
    part2("input2.txt")

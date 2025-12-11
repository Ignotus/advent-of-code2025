from collections import deque


def search(tree: dict[str, list[str]]) -> int:
    d = deque(["you"])
    c = 0
    while d:
        e = d.pop()
        for l in tree[e]:
            if l == "out":
                c += 1
            else:
                d.append(l)
    return c

def main(file_name: str):
    tree = dict()
    with open(file_name) as f:
        for l in f:
            root, *leaves = l[:-1].split(" ")
            tree[root[:-1]] = leaves

    print(search(tree))


if __name__ == "__main__":
    main("input1.txt")
    main("input2.txt")

import functools

def main(file_name: str, part: int):
    tree = dict()
    with open(file_name) as f:
        for l in f:
            root, *leaves = l[:-1].split(" ")
            tree[root[:-1]] = leaves

    @functools.cache
    def search(src: str, dst: str) -> int:
        if src == dst:
            return 1

        if src == "out":
            return 0

        return sum([search(l, dst) for l in tree[src]])

    if part == 0:
        print(search("you", "out"))
    else:
        print(
            search("svr", "fft") *
            search("fft", "dac") *
            search("dac", "out")
        )


if __name__ == "__main__":
    main("input1.txt", 0)
    main("input2.txt", 0)

    main("input3.txt", 1)
    main("input2.txt", 1)

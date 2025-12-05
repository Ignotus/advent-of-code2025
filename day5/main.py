def main(file_name: str):
    ranges = []

    def is_fresh(i: int):
        for x, y in ranges:
            if x <= i <= y:
                return True

        return False

    c = 0
    with open(file_name) as f:
        for l in f:
            if "-" in l:
                ranges.append(tuple(map(int, l.split("-"))))
            elif l[:-1].isnumeric() and is_fresh(int(l)):
                c += 1
    print("part1", c)

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges = [sorted_ranges[0]]
    for x, y in sorted_ranges[1:]:
        x0, y0 = merged_ranges[-1]
        if x <= y0: # merge ranges
            merged_ranges[-1] = (min(x, x0), max(y, y0))
        else:
            merged_ranges.append((x, y))

    r = sum(map(lambda x: x[1]-x[0]+1, merged_ranges))
    print("part2", r)

if __name__ == "__main__":
    main("input2.txt")

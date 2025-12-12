import numpy as np


def read_file(file_name: str):
    shapes = list()
    regions = list()
    shape = list()
    with open(file_name) as f:
        for l in f:
            if "x" in l:
                # regions
                size, quantity = l[:-1].split(":")
                size = list(map(int, size.split("x")))
                quantity = list(map(int, quantity.split()))
                regions.append((size, np.asarray(quantity)))
            elif "#" in l or "." in l:
                # shapes
                shape.append([1 if x == "#" else 0 for x in l[:-1]])
            elif ":" in l:
                # break point
                if shape:
                    shapes.append(np.asarray(shape))
                shape = list()

    shapes.append(np.asarray(shape))

    return regions, shapes


def main(file_name: str):
    regions, shapes = read_file(file_name)
    shape_areas = np.asarray([np.sum(shape) for shape in shapes])
    max_shape_area = max([s.shape[0] * s.shape[1] for s in shapes])

    c = 0
    for size, quantity in regions:
        area = size[0] * size[1]
        if np.sum(shape_areas * quantity) > area:
            continue

        if area // max_shape_area >= np.sum(quantity):
            c += 1
            continue

        assert False # Hope that we don't have to solve this case
    print(c)


if __name__ == "__main__":
    main("input2.txt")

import heapq
import itertools
from collections import Counter
import numpy as np


def merge_groups(groups: dict[int, int], i: int, j: int):
    group_id_j = groups[j]
    for k, v in groups.items():
        if v == group_id_j:
            groups[k] = groups[i]


def group(connections: list[tuple[int, tuple[int, int]]], n_boxes: int) -> dict[int, int]:
    """ Starting with n_boxes groups, we gradually merge them based on connections."""
    groups = {i : i for i in range(n_boxes)}
    for _, (i, j) in connections:
        if groups[i] != groups[j]:
            merge_groups(groups, i, j)

    return groups


def find_last_merge(connections: list[tuple[int, tuple[int, int]]], n_boxes: int) -> tuple[int, int]:
    groups = {i : i for i in range(n_boxes)}
    remaining_groups = set(groups.values())
    for _, (i, j) in connections:
        if groups[i] != groups[j]:
            if len(remaining_groups) == 2:
                return (i, j)

            remaining_groups.remove(groups[j])
            merge_groups(groups, i, j)


def group_product(groups: dict[int, int]) -> int:
    counter = Counter()
    for k, v in groups.items():
        counter[v] += 1

    return np.prod(list(sorted(counter.values(), reverse=True))[:3])


def main(file_name: str, n_connections: int, part: int):
    with open(file_name) as f:
        boxes = np.asarray([list(map(int, l.split(","))) for l in f])

    boxes_T = np.expand_dims(boxes.T, 0)
    # [N x 3 x 1]
    boxes = np.expand_dims(boxes, 2)
    # N x N
    distance = np.triu(np.sum((boxes - boxes_T) ** 2, 1), 0)
    distance[distance == 0] = np.iinfo(distance.dtype).max
    distance = distance.flatten()
    data = zip(distance, itertools.product(range(len(boxes)), range(len(boxes))))

    if part == 0:
        connections = heapq.nsmallest(n_connections, data, key=lambda x: x[0])
        print(group_product(group(connections, len(boxes))))
    else:
        connections = sorted(data, key=lambda x: x[0])
        i, j = find_last_merge(connections, len(boxes))
        print(boxes[i][0, 0] * boxes[j][0, 0])


if __name__ == "__main__":
    main("input1.txt", 10, 0)
    main("input2.txt", 1000, 0)
    main("input1.txt", 10, 1)
    main("input2.txt", 1000, 1)

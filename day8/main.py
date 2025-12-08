import heapq
import itertools
from collections import Counter
import numpy as np

def group(connections: list[tuple[int, tuple[int, int]]], n_boxes: int) -> int:
    """ when i -> j, and a -> b, and then later j -> ... -> a
        we should be able to combine all {i, j, a, b} as a single
        group.
    """
    groups = dict()
    new_group_id = -1
    for _, (i, j) in connections:
        if i in groups and j not in groups:
            groups[j] = groups[i]
        elif i not in groups and j in groups:
            groups[i] = groups[j]
        elif i not in groups and j not in groups:
            new_group_id += 1
            groups[i] = new_group_id
            groups[j] = new_group_id
        elif i != j: # both i, j in groups
            group_id_j = groups[j]
            for k, v in groups.items():
                if v == group_id_j:
                    groups[k] = groups[i]

    for i in range(n_boxes):
        if i not in groups:
            new_group_id += 1
            groups[i] = new_group_id

    counter = Counter()
    for k, v in groups.items():
        counter[v] += 1

    return np.prod(list(sorted(counter.values(), reverse=True))[:3])


def main(file_name: str, n_connections: int):
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

    connections = heapq.nsmallest(n_connections, data, key=lambda x: x[0])
    print(group(connections, len(boxes)))


if __name__ == "__main__":
    main("input1.txt", 10)
    main("input2.txt", 1000)

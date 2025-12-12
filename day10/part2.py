import re
import numpy as np
import pulp

def parse_line(l: str):
    m = re.match(r"\[([.#]+)\] ((\([\d,]+\) )+){([\d,]+)}", l)
    wirings = [
        [int(y) for y in x[1:-1].split(",")]
        for x in m.group(2).split()
    ]

    joltage_req = np.asarray([int(x) for x in m.group(4).split(",")])

    new_wirings = list()
    for wiring in wirings:
        hot_vec = np.zeros(len(joltage_req), dtype=np.int64)
        for w in wiring:
            hot_vec[w] = 1
        new_wirings.append(hot_vec)
    new_wirings = np.asarray(new_wirings)

    return new_wirings.T, joltage_req


def solve(wirings: np.ndarray, joltage_req: np.ndarray) -> int:
    bounds = (0, None)

    model = pulp.LpProblem("Integer Minimization Problem", pulp.LpMinimize)
    n_vars = wirings.shape[1]
    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat=pulp.LpInteger) for i in range(n_vars)]

    model += pulp.lpSum(x), "Objective Function"

    for i in range(wirings.shape[0]):
        lhs = pulp.lpSum(wirings[i, j] * x[j] for j in range(n_vars))
        rhs = joltage_req[i]
        model += (lhs == rhs), f"Constraint_{i}"

    model.solve()
    x_solution = np.array([pulp.value(var) for var in x])
    return sum(x_solution)


def main(file_name: str):
    with open(file_name) as f:
        data = list(map(parse_line, f))

    c = 0
    for wirings, joltage_req in data:
        c += solve(wirings, joltage_req)

    print(c)



if __name__ == "__main__":
    main("input1.txt")
    main("input2.txt")

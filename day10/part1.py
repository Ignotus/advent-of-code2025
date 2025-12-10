import re
import functools

def parse_line(l: str):
    m = re.match(r"\[([.#]+)\] ((\([\d,]+\) )+){([\d,]+)}", l)
    indicators = m.group(1)
    wirings = [
        tuple(int(y) for y in x[1:-1].split(","))
        for x in m.group(2).split()
    ]
    joltage_req = [int(x) for x in m.group(4).split(",")]

    return indicators, wirings, joltage_req

@functools.cache
def push(indicators: str, button_wiring: tuple[int, ...]) -> str:
    new_indicators = list(indicators)
    for i in button_wiring:
        new_indicators[i] = "." if indicators[i] == "#" else "#"
    new_indicators = "".join(new_indicators)
    return new_indicators


def try_n_push(indicators: str, indicators_gt: str, wirings: list[tuple[int, ...]]) -> int:
    indicator_states = [indicators]

    new_indicator_states = list()

    n_press = 0
    while True:
        n_press += 1
        for indicator_state in indicator_states:
            for wiring in wirings:
                new_indicators = push(indicator_state, wiring)
                if new_indicators == indicators_gt:
                    return n_press

                new_indicator_states.append(new_indicators)
        indicator_states = new_indicator_states
        new_indicator_states = list()


def main(file_name: str):
    with open(file_name) as f:
        data = list(map(parse_line, f))

    c = 0
    for indicators_gt, wirings, _ in data:
        c += try_n_push("." * len(indicators_gt), indicators_gt, wirings)
    print(c)


if __name__ == "__main__":
    main("input1.txt")
    main("input2.txt")

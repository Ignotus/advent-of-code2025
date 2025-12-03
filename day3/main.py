import numpy as np

def largest_joltage(l: str, num_digit: int=2) -> int:
    digits = list(map(int, l))

    digit_pos = -1
    res = []
    for i in range(num_digit - 1, -1, -1):
        digit_pos = np.argmax(digits[digit_pos+1:len(digits)-i]) + digit_pos + 1
        digit = digits[digit_pos]
        res.append(digit)

    return int("".join(map(str, res)))


def main(file_name: str, num_digit: int):
    s = 0
    with open(file_name) as f:
        for l in f:
            num = largest_joltage(l.strip(), num_digit)
            s += num
    print(s)


if __name__ == "__main__":
    main("input2.txt", 2)
    main("input2.txt", 12)

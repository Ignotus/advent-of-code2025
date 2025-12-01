class Dial:
    def __init__(self):
        self.d = 50

    def left(self):
        self.d = (self.d - 1) % 100

    def right(self):
        self.d = (self.d + 1) % 100


def part1():
    dial = Dial()
    c = 0
    with open("input.txt", "r") as f:
        for l in f:
            step = int(l[1:])
            side = l[0]
            for i in range(step):
                if side == "R":
                    dial.right()
                else:
                    dial.left()
            if dial.d == 0:
                c += 1
    print(c)


def part2():
    dial = Dial()
    c = 0
    with open("input.txt", "r") as f:
        for l in f:
            step = int(l[1:])
            side = l[0]
            for i in range(step):
                if side == "R":
                    dial.right()
                else:
                    dial.left()
                if dial.d == 0:
                    c+= 1
    print(c)


if __name__ == "__main__":
    part1()
    part2()

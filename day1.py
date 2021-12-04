

def part1():
    with open('inputs/day1.txt', 'r') as f:
        d1 = [int(i) for i in f.read().split()]
    increase = 0
    for i in range(1, len(d1)):
        if d1[i] > d1[i - 1]:
            increase += 1
    print(increase)


def part2():
    with open('inputs/day1.txt', 'r') as f:
        d1 = [int(i) for i in f.read().split()]
    increases = 0
    for i in range(len(d1) - 3):
        if d1[i] + d1[i+1] + d1[i+2] < d1[i+1] + d1[i+2] + d1[i+3]:
            increases += 1
    print(increases)


part1()
part2()

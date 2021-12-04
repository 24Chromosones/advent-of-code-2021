def part1():
    with open('inputs/day2.txt', 'r') as f:
        d2 = f.read().split('\n')
    horizontal = 0
    depth = 0
    d2 = [line for line in d2 if line.strip() != '']
    for i in d2:
        direction, num = i.split()[0], i.split()[1]
        num = int(num)
        if direction == 'forward':
            horizontal += num
        elif direction == 'down':
            depth += num
        elif direction == 'up':
            depth -= num
    print(horizontal * depth)

def part2():
    with open('inputs/day2.txt', 'r') as f:

        d2 = f.read().split('\n')
    horizontal = 0
    depth = 0
    aim = 0
    d2 = [line for line in d2 if line.strip() != '']
    for i in d2:
        direction, num = i.split()[0], i.split()[1]
        num = int(num)
        if direction == 'forward':
            horizontal += num
            depth += aim * num
        elif direction == 'down':
            aim += num
        elif direction == 'up':
            aim -= num
    print(horizontal * depth)

part1()
part2()
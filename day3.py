def part1():
    with open('inputs/day3.txt', 'r') as f:
        d3 = [line for line in f.read().split() if line.strip() != '']
    gamma = ''
    for i in range(len(d3[0])):
        one_count = 0
        zero_count = 0
        for report in d3:
            if report[i] == '1':
                one_count += 1
            else:
                zero_count += 1
        gamma += '1' if one_count > zero_count else '0'
    epsilon = ''.join(['0' if x == '1' else '1' for x in gamma])
    print(int(gamma, 2) * int(epsilon, 2))


def part2():
    with open('inputs/day3.txt', 'r') as f:
        d3 = [line for line in f.read().split() if line.strip() != '']
    o2_d3 = d3
    co2_d3 = d3
    line_length = len(d3[0])
    for i in range(line_length):
        o2_one_count, o2_zero_count = 0, 0
        co2_one_count, co2_zero_count = 0, 0
        for report in o2_d3:
            if report[i] == '1':
                o2_one_count += 1
            else:
                o2_zero_count += 1
        for report in co2_d3:
            if report[i] == '1':
                co2_one_count += 1
            else:
                co2_zero_count += 1
        o2_criteria = '1' if o2_one_count >= o2_zero_count else '0'
        co2_criteria = '0' if co2_zero_count <= co2_one_count else '1'

        if len(o2_d3) != 1:
            o2_d3 = [x for x in o2_d3 if x[i] == o2_criteria]
        if len(co2_d3) != 1:
            co2_d3 = [x for x in co2_d3 if x[i] == co2_criteria]
    print(int(o2_d3[0], 2) * int(co2_d3[0], 2))


part1()
part2()

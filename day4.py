#  We dont talk about day 4
# This is the worst code ive ever written but i finally got the answer

def part1():
    with open('inputs/day4.txt', 'r') as f:
        d4 = f.read().split('\n\n')


    numbers = d4[0].split(',')
    games = {}
    for i in range(1, len(d4)):
        games[f'game{i}'] = d4[i].split('\n')
        games[f'game{i}'] = [line for line in games[f'game{i}'] if line.strip() != '']
    first = True
    for i in numbers:
        for game in games:
            for row in range(len(games[game])):
                if first:
                    games[game][row] = games[game][row].split()
                games[game][row] = ['-1' if x == i else x for x in games[game][row]]
                equal_number = games[game][row][0]
                check = True
                for o in games[game][row]:
                    if equal_number != o:
                        check = False
                        break
                if check:
                    print(games[game][row] + 'a')
                    answer = 0
                    for j in games[game]:
                        for num in j:
                            if num != '-1':
                                answer += int(num)
                    return answer * int(i)
            for j in range(len(games[game])):
                column = []
                for k in games[game]:
                    column.append(k[j])
                equal_number = games[game][row][0]
                check = True
                for o in column:
                    if equal_number != o:
                        check = False
                        break
                if check:
                    answer = 0
                    for v in games[game]:
                        for num in v:
                            if num != '-1':

                                answer += int(num)
                    return answer * int(i)
        first = False


print(part1())
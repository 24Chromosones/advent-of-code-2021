def part1():
    with open('inputs/day4.txt', 'r') as f:
        d4 = f.read().split('\n\n')


    numbers = d4[0].split(',')
    games = {}
    for i in range(1, len(d4)):
        games[f'game{i}'] = d4[i].split('\n')
        games[f'game{i}'] = [line for line in games[f'game{i}'] if line.strip() != '']
        # for j in range(len(games[f'game{i}'])):
        #     print(games[f'game{i}'][j])
        # print('\n')
    first = True
    for i in numbers:
        for game in games:
            for row in range(len(games[game])):
                # print(games[game][row])
                # print(row)
                if first:
                    games[game][row] = games[game][row].split()
                    first = False
                games[game][row] = ['-1' if x == i else x for x in games[game][row]]
                if all(games[game][row]):
                    answer = 0
                    for j in game:
                        for num in j:
                            if num != '-1':
                                answer += int(num)
                                return answer
        for k in range(len(game[]))

            


part1()
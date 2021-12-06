def part1():
    with open('inputs/day4.txt', 'r') as f:
        d4 = f.read()
    d4 = d4.split('\n\n')
    numbers = d4[0].split(',')
    games = {}
    for i in range(1, len(d4)):
        games[f'game{i}'] = d4[i].split('\n')
        # for j in range(len(games[f'game{i}'])):
        #     print(games[f'game{i}'][j])
        # print('\n')

    for i in numbers:
        for game in games:
            print(game)
            for row in range(len(games[game])):
                print(games[game][row])
                print(row)
                games[game][row] = games[game][row].split()
                games[game][row] = ['-1' if x == i else x for x in games[game][row]]
            


part1()
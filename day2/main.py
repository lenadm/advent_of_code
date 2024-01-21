import re
file = open('./input', 'r')

def part1():
    possible = {'red':12, 'green':13, 'blue':14}
    bad_sum = 0
    sum = 0
    for line in file:
        first_time = True
        game = re.search(r'\d+', line)
        results = re.finditer(r'(\d+) (red|blue|green)', line)
        for matches in results:
            if first_time == True:
                split = matches.group().split()
                if int(split[0]) > possible[split[1]]:
                    first_time = False
                    bad_sum += int(game.group())
        sum += int(game.group())

    print(sum - bad_sum)

def part2():
    sum = 0
    for line in file:
        local_sum = 1
        highest = {'red':0, 'green':0, 'blue':0}
        results = re.finditer(r'(\d+) (red|blue|green)', line)
        for matches in results:
            split = matches.group().split()
            if int(split[0]) > highest[split[1]]:
                   highest[split[1]] = int(split[0])
                   print(highest)

        for number in highest.values():
            local_sum *= number
        sum += local_sum
        print(highest)

    print(sum)

part2()

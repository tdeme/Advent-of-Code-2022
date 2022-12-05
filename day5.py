def solve(stacks, lines):
    instructions = []
    for line in lines:
        instructions.append(line.split(' '))


    for i,instruction in enumerate(instructions):
        transport = []
        for i in range(int(instruction[1])):
            transport.append(stacks[int(instruction[3])].pop(0))

        transport.reverse()
        for char in transport:
            stacks[int(instruction[5])].insert(0, char)
        print(stacks)

    result = ''
    for i in range(1, 10):
        if i in stacks.keys():
            result += stacks[i][0]

    return result


def fill_stacks(lines):
    stacks = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for line in lines:
        for i,char in enumerate(line):
            if char.lower() in alpha:
                if (i//4) +1 not in stacks:
                    stacks[(i//4)+1] = [char]
                else:
                    stacks[(i//4)+1].append(char)

    return stacks


def main():
    text = open('day5input.txt', 'r')
    lines = []
    for line in text:
        lines.append(line.rstrip())

    stacks = fill_stacks(lines[:8])
    '''lines = ['move 1 from 2 to 1',
            'move 3 from 1 to 3',
            'move 2 from 2 to 1',
            'move 1 from 1 to 2']
    
    stacks = {1:['N','Z'], 2:['D','C','M'], 3:['P']}'''

    print(solve(stacks, lines[10:]))


if __name__ == '__main__':
    main()
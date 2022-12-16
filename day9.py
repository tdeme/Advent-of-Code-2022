def solve(moves):
    positions = [(0,0)]
    head = [0,0]
    knots = {0: head}

    for i in range(1,10):
        knots[i] = [0,0]

    for move in moves:
        for _ in range(int(move[1])):
            if move[0]=='R':
                head[0]+=1
            elif move[0]=='L':
                head[0]-=1
            elif move[0]=='U':
                head[1]+=1
            elif move[0]=='D':
                head[1]-=1

            for i in range(1,10):
                knots[i] = check(head, knots, i)

            if tuple(knots[9]) not in positions:
                positions.append(tuple(knots[9]))


    return len(positions)


def check(head, knots, i):
    x = abs(knots[i-1][0]-knots[i][0])**2
    y = abs(knots[i-1][1]-knots[i][1])**2
    if abs(x+y)**0.5>1.42:
        knots[i] = update(knots[i-1], knots[i])

    return knots[i]

def update(head, tail):
    if head[0]>tail[0]:
        tail[0]+=1
    elif head[0]<tail[0]:
        tail[0]-=1
    if head[1]>tail[1]:
        tail[1]+=1
    elif head[1]<tail[1]:
        tail[1]-=1

    return tail


def main():
    text = open('day9input.txt', 'r')
    lines = []
    for line in text:
        lines.append(line.rstrip())


    moves = [line.split(' ') for line in lines]
    
    print(solve(moves))


if __name__ == '__main__':
    main()
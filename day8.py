def solve(lines):
    '''Part 1:
    visibles = 0
    visibles+=2*len(lines)
    visibles+=2*len(lines[0])
    visibles-=4 #We counted the corners twice

    for row in range(1, len(lines)-1):
        for col in range(1, len(lines[0])-1):
            if is_visible(lines, row, col):
                visibles+=1
                print(lines[row][col], 'at', row, col, 'is visible')

    return visibles'''


    #Part 2:
    scores = []
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            scores.append(calc_score(lines, row, col))

    return max(scores)


def calc_score(lines, row, col):
    return count_right(lines,row,col)*count_left(lines,row,col)*count_down(lines,row,col)*count_up(lines,row,col)


def count_right(lines, row, col):
    count = 0
    for i in range(col+1, len(lines[0])):
        count+=1
        if lines[row][i]>=lines[row][col]:
            break
    return count


def count_left(lines, row, col):
    count = 0
    for i in range(col-1, -1, -1):
        count+=1
        if lines[row][i]>=lines[row][col]:
            break
    return count


def count_down(lines, row, col):
    count = 0
    for i in range(row+1, len(lines)):
        count+=1
        if lines[i][col]>=lines[row][col]:
            break
    return count


def count_up(lines, row, col):
    count = 0
    for i in range(row-1, -1, -1):
        count+=1
        if lines[i][col]>=lines[row][col]:
            break
    return count


def is_visible(lines, row, col):
    if check_left(lines, row, col) or check_right(lines, row, col) or check_up(lines, row, col) or check_down(lines, row, col):
        return True

    return False


def check_right(lines, row, col):
    if lines[row][col]>max(lines[row][:col]):
        return True

    return False

def check_left(lines, row, col):
    if lines[row][col]>max(lines[row][col+1:]):
        return True

    return False

def check_down(lines, row, col):
    if lines[row][col]>max([lines[i][col] for i in range(row)]):
        return True

    return False

def check_up(lines, row, col):
    if lines[row][col]>max([lines[i][col] for i in range(row+1, len(lines))]):
        return True

    return False
        

def main():
    text = open('day8input.txt', 'r')
    lines = []
    for line in text:
        lines.append(line.rstrip())
        
    #lines = ['30373', '25512', '65332', '33549', '35390']

    lines = [[int(num) for num in line] for line in lines]

    print(solve(lines))


if __name__ == '__main__':
    main()
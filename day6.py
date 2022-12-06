def find_start(lines):
    for i in range(13, len(lines[0])):
        diff = True
        for char in lines[0][i-13:i+1]:
            if lines[0][i-13:i+1].count(char) > 1:
                diff = False
                break
        if diff:
            return i+1


def main():
    text = open('day6input.txt', 'r')
    lines = []
    for line in text:
        lines.append(line.rstrip())
        
    print(find_start(lines))


if __name__ == '__main__':
    main()
def score(lines):
    total = 0
    for line in lines:
        if line[-1]=='X':
            if line[0]=='A':
                total+=3
            elif line[0]=='C':
                total+=2
            else:
                total+=1
        elif line[-1]=='Y':
            total+=3
            if line[0]=='B':
                total+=2
            elif line[0]=='A':
                total+=1
            else:
                total+=3
        else:
            total+=6
            if line[0]=='C':
                total+=1
            elif line[0]=='B':
                total+=3
            else:
                total+=2
    return total
            
def main():
    text = open('day2input.txt', 'r')
    lines = []
    for line in text:
        lines.append(line.rstrip())
    print(score(lines))


if __name__ == '__main__':
    main()
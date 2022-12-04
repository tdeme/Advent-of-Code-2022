def count_overlaps(pairs):
    count = 0
    for pair in pairs:
        range1 = pair[0].split('-')
        range2 = pair[1].split('-')
        if int(range1[0])<=int(range2[0])<=int(range1[1]) or int(range1[0])<=int(range2[1])<=int(range1[1]):
            count+=1
        elif int(range2[0])<=int(range1[0])<=int(range2[1]) or int(range2[0])<=int(range1[1])<=int(range2[1]):
            count+=1

    return count

def main():
    text = open('day4input.txt', 'r')
    lines = []
    for line in text:
        lines.append(line.rstrip())
    pairs = []
    for pair in lines:
        pairs.append(pair.split(','))

    print(count_overlaps(pairs))


if __name__ == '__main__':
    main()
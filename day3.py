def solve(sacks):
    total = 0
    for i in range(0, len(sacks), 3):
        for char in sacks[i]:
            if char in sacks[i+1] and char in sacks[i+2]:
                total+=priority(char)
                break

    return total

def priority(char):
    priorities = {}
    for i,c in enumerate('abcdefghijklmnopqrstuvwxyz'):
        priorities[c] = i+1

    if char!=char.lower():
        priorities[char] = priorities[char.lower()]+26

    print(priorities)
    return priorities[char]
    



def main():
    text = open('day3input.txt', 'r')
    sacks = []
    for line in text:
        sacks.append(line.rstrip())
    
    print(solve(sacks))


if __name__ == '__main__':
    main()
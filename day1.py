def find_most(nums):
    elves = []
    s = 0
    for num in nums:
        try:
            s+=int(num)

        except:
            elves.append(s)
            s = 0
    
    elves.sort()
    return sum(elves[-3:])

def main():
    text = open('day1input.txt', 'r')
    nums = []
    for line in text:
        nums.append(line.rstrip())
    print(find_most(nums))


if __name__ == '__main__':
    main()
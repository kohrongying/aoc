def solve1(filename, num_batt=2):
    with open(filename) as f:
        lines = f.readlines()
    
    joltage = 0
    for line in lines:
        line = line.strip()
        joltage += get_battery2(line, num_batt)
    print('joltage is ', joltage)
    
# Part 1 naiive answer
def get_battery(line: str) -> int:
    maxDigit = 0
    maxIdx = 0
    for i, ch in enumerate(line):
        if int(ch) > maxDigit:
            maxDigit = int(ch)
            maxIdx = i
    # check edge case if maxIdx is at end of string
    if maxIdx == len(line) - 1:
        partition = line[:maxIdx]
    else:
        partition = line[maxIdx+1:]
    secondMax = 0
    for i in partition:
        secondMax = max(secondMax, int(i))
    if maxIdx == len(line) - 1:
        ret = int(f'{secondMax}{maxDigit}')
    else:
        ret = int(f'{maxDigit}{secondMax}')
    # print(ret)
    return ret

# Works for both part 1 and 2
# Given a line, start searching for the max with a range of the startIdx to the end - num batt.
# eg. 234234234234278: Find 7 from [23423423423427] then find 8 from [8]
# eg. 818181911112111: Find 9 from [81818191111211] then find 2 from [11112111]
def get_battery2(line: str, num_batt=12) -> int:
    numms = [int(i) for i in line]
    ret = 0
    currMaxIdx = -1
    for i in range(num_batt):
        currMax = 0
        for j in range(currMaxIdx+1, len(numms)-num_batt+1+i):
            if numms[j] > currMax:
                currMax = numms[j]
                currMaxIdx = j
        ret = ret * 10 + currMax
    return ret
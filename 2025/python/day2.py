def solve1(filename):
    with open(filename) as f:
        lines = f.readlines()
    a = []
    for line in lines:
        line = line.strip()
        a.extend(line.split(','))
    summ = 0
    for line in a:
        first, last = line.split('-')
        s = get_invalid1(int(first), int(last))
        summ += sum(s)
    print('summ is ', summ)
    
def solve2(filename):
    with open(filename) as f:
        lines = f.readlines()
    a = []
    for line in lines:
        line = line.strip()
        a.extend(line.split(','))
    summ = 0
    for line in a:
        first, last = line.split('-')
        s = get_invalid2(int(first), int(last))
        summ += sum(s)
    print('summ is ', summ)
        
def get_invalid1(first, second):
    all_ranges = list(range(first, second+1))
    
    def is_invalid(num): #1212 is True, 123 is False
        if len(str(num)) % 2 != 0:
            return False    
        s = str(num)
        part = s[:len(s) // 2]
        if (part * 2) == s:
            return True
        return False
    
    s = [i for i in all_ranges if is_invalid(i)]
    # print(s)
    return s
    
    
def get_invalid2(first, second):
    all_ranges = list(range(first, second+1))
    
    def is_invalid(num): #111 is True, 123123 is True
        s = str(num)
        for i in range(len(s) // 2):
            part = s[:i+1]
            if len(s) % len(part) != 0:
                continue
            num_parts = len(s) // len(part)
            if (part * num_parts) == s:
                return True
        
        return False
    
    s = [i for i in all_ranges if is_invalid(i)]
    print(s)
    return s
    
# assert get_invalid(11,22) == [11,22]
# assert get_invalid(95,115) == [99]
# assert get_invalid(998,1012) == [1010]

assert get_invalid2(11,22) == [11,22]
assert get_invalid2(95,115) == [99, 111]
assert get_invalid2(998,1012) == [999, 1010]
assert get_invalid2(446443, 446449) == [446446]

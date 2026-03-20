## haha, brute force using a dictionary does not work (adding full range of fresh ingred to dict takes too long)
def solve1(filename):
    freshraw = []
    counter = 0
    with open(filename) as f:
        lines = f.readlines()
        isAvail = False
        for line in lines:
            if line.strip() == '':
                isAvail = True
                freshraw = sorted(freshraw, key=lambda x: x[0])
                continue
            
            if not isAvail:
                lower, upper = line.strip().split('-')
                freshraw.append((int(lower), int(upper)))
            else:
                target = int(line.strip())
                for i in freshraw:
                    if target < i[0]:
                        break
                    if is_in_range(target, i[0], i[1]):
                        counter += 1
                        break
                
    print(counter)
    return counter

def is_in_range(target: int, lower: int, upper: int) -> bool:
    if target < lower:
        return False
    return lower <= target <= upper
          

# Merge ranges question on leetcode lol          
def solve2(filename):
    freshraw = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == '':
                break
            lower, upper = line.strip().split('-')
            freshraw.append((int(lower), int(upper)))
            
    freshraw = sorted(freshraw, key=lambda x: x[0])
    merged = merge_ranges(freshraw)
    counter = get_distinct_from_range(merged)
    print(counter)
    return counter
    
    
def merge_ranges(fresh: list[tuple[int, int]])-> list[tuple[int,int]]:
    if len(fresh) == 0:
        return fresh
    ret = [fresh[0]]
    for curr in range(1, len(fresh)):
        a, b = ret[-1]
        c, d = fresh[curr]
        """
        (a, b) vs (c, d) -> assumes a <= c <= d. 
        b can be 
        1) a <= b < c <= d -> (a,b), (c,d) non-overlapping
        """
        if c > b:
            ret.append(fresh[curr])
            continue
        """
        1) a <= c <= d <= b -> (a, b) overlapping)
        2) a <= c <= b <= d -> (a, d) overlapping
        """
        # Now C is <= b
        if b >= d:
            ret[-1] = (a, b) # no change
        else:
            ret[-1] = (a, d) # merge
        
    return ret

def get_distinct_from_range(fresh: list[tuple[int, int]])-> int:
    counter = 0
    for i in fresh:
        counter += i[1] - i[0] + 1 
    return counter


assert merge_ranges([(3,5), (10,14), (12,18), (16,20)]) == [(3,5), (10,20)]
assert get_distinct_from_range([(3,5), (10,20)]) == 3 + 11

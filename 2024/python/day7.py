# (result, [number])
inp = []


def read_inputs():
    with open('input/day7.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            result, nums = line.split(':')
            arr = []
            for x in nums.split(" "):
                if x:
                    arr.append(int(x))
            inp.append((int(result), arr))


def evaluate_operation(lst: list[int], ans: int) -> bool:
    if len(lst) == 1 and lst[0] == ans:
        return True
    if len(lst) == 1 and lst[0] != ans:
        return False
    result = evaluate_operation([lst[0] + lst[1]] + lst[2:], ans) or \
             evaluate_operation([lst[0] * lst[1]] + lst[2:], ans)
    return result


def evaluate_operation2(lst: list[int], ans: int) -> bool:
    if len(lst) == 1 and lst[0] == ans:
        return True
    if len(lst) == 1 and lst[0] != ans:
        return False
    if lst[0] > ans:
        return False
    result = evaluate_operation2([lst[0] + lst[1]] + lst[2:], ans) or \
             evaluate_operation2([lst[0] * lst[1]] + lst[2:], ans) or \
             evaluate_operation2([int(str(lst[0]) + str(lst[1]))] + lst[2:], ans)

    return result


def solve1():
    ans = 0
    for line in inp:
        if evaluate_operation(line[1], line[0]):
            ans += line[0]
    print('Ans is', ans)


def solve2():
    ans = 0
    for line in inp:
        if evaluate_operation2(line[1], line[0]):
            ans += line[0]
    print('Ans is', ans)


import timeit

if __name__ == "__main__":
    read_inputs()
    # solve1()
    timer = timeit.Timer(lambda: solve2())
    elapsed = timer.timeit(1)
    print(f'Time taken: {elapsed:.6f} seconds')

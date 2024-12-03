left = []
right = []


def read_inputs():
    with open('input/day1.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            arr = line.split(" ")
            left.append(int(arr[0]))
            right.append(int(arr[-1]))


def solve1():
    left.sort()
    right.sort()

    sum_diffs = 0
    for i, j in zip(left, right):
        sum_diffs += abs(i - j)
    print('Difference score is', sum_diffs)


def solve2():
    right_occurrences = {}
    for num in right:
        right_occurrences[str(num)] = right_occurrences.get(str(num), 0) + 1

    similarity_score = 0
    for digit in left:
        num_occurrences = right_occurrences.get(str(digit), 0)
        similarity_score += num_occurrences * digit
    print('Similarity Score is', similarity_score)


if __name__ == "__main__":
    read_inputs()
    # solve1()
    solve2()

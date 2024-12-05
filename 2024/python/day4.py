# 2D array
inp = []
num_rows = 0
num_cols = 0


def read_inputs():
    with open('input/day4.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            tmp = []
            for ch in line.strip():
                tmp.append(ch)
            inp.append(tmp)
    global num_rows, num_cols
    num_rows = len(inp)
    num_cols = len(inp[0])


def is_valid_coordinate(x, y):
    return 0 <= x < num_cols and 0 <= y < num_rows


def solve1():
    def get_possibilities(x, y):
        p = []
        possibilities = [
            [(x, y), (x - 1, y), (x - 2, y), (x - 3, y)],  # vertical D->U
            [(x, y), (x + 1, y - 1), (x + 2, y - 2), (x + 3, y - 3)],  # diagonal to northeast
            [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)],  # horizontal L->R
            [(x, y), (x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3)],  # diagonal to southeast
            [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)],  # vertical U->D
            [(x, y), (x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3)],  # diagonal to southwest
            [(x, y), (x, y - 1), (x, y - 2), (x, y - 3)],  # horizontal R->L,
            [(x, y), (x - 1, y - 1), (x - 2, y - 2), (x - 3, y - 3)],  # diagonal to northwest
        ]
        for pos in possibilities:
            if all([is_valid_coordinate(t[0], t[1]) for t in pos]):
                p.append(pos)
        return p

    def determine_word(coordinates):
        # coordinates is a list of tuples
        return ''.join([inp[coor[0]][coor[1]] for coor in coordinates])

    count = 0
    for row in range(len(inp)):
        for i in range(len(inp[row])):
            ch = inp[row][i]
            if ch != 'X':
                continue
            for pos in get_possibilities(row, i):
                if determine_word(pos) == 'XMAS':
                    count += 1
    print('Count:', count)


def solve2():
    # taking 'A' as the central starting point
    def get_possibilities(x, y):
        p = []
        possibilities = [
            [(x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)],  # corners
        ]
        for pos in possibilities:
            if all([is_valid_coordinate(t[0], t[1]) for t in pos]):
                p.append(pos)
        return p

    def determine_word(coordinates):
        # coordinates is a list of tuples
        return ''.join([inp[coor[0]][coor[1]] for coor in coordinates])

    count = 0
    for row in range(len(inp)):
        for i in range(len(inp[row])):
            ch = inp[row][i]
            if ch != 'A':
                continue
            for pos in get_possibilities(row, i):
                if determine_word(pos) in ['MMSS', 'MSMS', 'SMSM', 'SSMM']:
                    count += 1
    print('Count:', count)


if __name__ == "__main__":
    read_inputs()
    solve1()
    solve2()

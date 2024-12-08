from dataclasses import dataclass
from typing import Tuple, Optional

inp = []
columns = []
guard_starting: Tuple[int, int] = (0, 0)
num_rows, num_cols = 0, 0


# frozen=True makes it immutable and adds a hash method (unable to use as cannot set 'next' for first node
# use eq=True to define own hash instead
@dataclass(eq=True)
class DirectionNode:
    name: str
    value: Tuple[int, int]
    next: Optional['DirectionNode'] = None

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f'Direction={self.name}'


def read_inputs():
    with open('input/day6.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            tmp = []
            for j, ch in enumerate(line.strip()):
                tmp.append(ch)
                if ch == '^':
                    global guard_starting
                    guard_starting = (i, j)
            inp.append(tmp)
    global num_rows, num_cols, columns
    num_rows = len(inp)
    num_cols = len(inp[0])
    for i in range(num_cols):
        tmp = []
        for row in inp:
            tmp.append(row[i])
        columns.append(tmp)


left_direction = DirectionNode(name='left', value=(0, -1))
down_direction = DirectionNode(name='down', value=(1, 0), next=left_direction)
right_direction = DirectionNode(name='right', value=(0, 1), next=down_direction)
up_direction = DirectionNode(name='up', value=(-1, 0), next=right_direction)
left_direction.next = up_direction


def is_valid_coordinate(x, y):
    return 0 <= x < num_cols and 0 <= y < num_rows


def solve1():
    guard_visited = [guard_starting]
    guard_curr_direction = up_direction
    guard_curr_pos = guard_starting
    while True:
        x = guard_curr_pos[0] + guard_curr_direction.value[0]
        y = guard_curr_pos[1] + guard_curr_direction.value[1]
        if is_valid_coordinate(x, y):
            if inp[x][y] != '#':
                guard_curr_pos = (x, y)
                guard_visited.append(guard_curr_pos)
            else:
                guard_curr_direction = guard_curr_direction.next
        else:
            break
    print('Ans:', len(set(guard_visited)))
    return set(guard_visited)


def get_corner_before_wall_in_row(curr_coor , direction):
    row_num, starting_column = curr_coor[0], curr_coor[1]
    try:
        if direction < 0:
            arr = list(reversed(inp[row_num][:starting_column]))
            return row_num, starting_column - arr.index('#')  # plus 1 to get pos before turn
        else:
            return row_num, starting_column + inp[row_num][starting_column + 1:].index(
                '#')  # minus 1 to get pos before turn
    except ValueError:
        return None


def get_corner_before_wall_in_col(curr_coor, direction):
    starting_row, column_num = curr_coor[0], curr_coor[1]
    try:
        column_values = columns[column_num]
        if direction < 0:
            arr = list(reversed(column_values[:starting_row]))
            return starting_row - arr.index('#'), column_num  # plus 1 to get pos before turn
        else:
            arr = column_values[starting_row + 1:]
            return starting_row + arr.index('#'), column_num  # minus 1 to get pos before turn
    except ValueError:
        return None


def solve2(positions):
    obstacles = 0

    def get_corner_or_out(curr_coor: Tuple[int, int], curr_dir: DirectionNode) -> Optional[Tuple[int, int]]:
        if curr_dir == up_direction:
            return get_corner_before_wall_in_col(curr_coor, -1)
        elif curr_dir == down_direction:
            return get_corner_before_wall_in_col(curr_coor, 1)
        elif curr_dir == left_direction:
            return get_corner_before_wall_in_row(curr_coor, -1)
        elif curr_dir == right_direction:
            return get_corner_before_wall_in_row(curr_coor, 1)
        else:
            print('hmmm unknown direction')

    for coor in positions:
        inp[coor[0]][coor[1]] = '#'
        columns[coor[1]][coor[0]] = '#'
        guard_visited = [(guard_starting, up_direction)]
        guard_curr_direction = up_direction
        guard_curr_pos = guard_starting
        while True:
            guard_curr_pos = get_corner_or_out(guard_curr_pos, guard_curr_direction)
            guard_curr_direction = guard_curr_direction.next

            # Made it out without looping
            if guard_curr_pos is None:
                break

            # Started to loop
            if (guard_curr_pos, guard_curr_direction) in guard_visited:
                obstacles += 1
                break
            else:
                guard_visited.append((guard_curr_pos, guard_curr_direction))

        # Reset to original
        inp[coor[0]][coor[1]] = '.'
        columns[coor[1]][coor[0]] = '.'

    print('Ans:', obstacles)


if __name__ == "__main__":
    read_inputs()
    positions = solve1()
    solve2(positions)

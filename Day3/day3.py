import sys
from collections import defaultdict

# {
#   row (int): {
#       col (int): wire_id (int)
#   }
# }
coordinates = defaultdict(lambda: dict())
crossing_coords = []
shortest_distance = None


def register_wire_step(wire, coord_col, coord_row):
    global shortest_distance, coordinates

    if coord_col in coordinates[coord_row].keys() and coordinates[coord_row][coord_col] != wire:
        crossing_coords.append((coord_row, coord_col))
        distance = abs(coord_col) + abs(coord_row)
        shortest_distance = distance if shortest_distance is None else min(distance, shortest_distance)
    else:
        coordinates[coord_row][coord_col] = wire


def get_step_coord_series(current_row, current_col, step):
    step_type = step[0]
    step_amount = int(step[1:])
    for _ in range(step_amount):
        current_row, current_col = {
            'D': lambda row, col: (row + 1, col),
            'R': lambda row, col: (row, col + 1),
            'U': lambda row, col: (row - 1, col),
            'L': lambda row, col: (row, col - 1)
        }[step_type](current_row, current_col)
        yield current_row, current_col


def get_all_wire_coords(paths, wire_id):
    current_row = 0
    current_col = 0
    for step in paths[wire_id]:
        for new_row, new_col in get_step_coord_series(current_row, current_col, step):
            current_row = new_row
            current_col = new_col
            yield current_row, current_col


def find_crossings(paths):
    for wire_id in range(len(paths)):
        for row, col in get_all_wire_coords(paths, wire_id):
            register_wire_step(wire_id, row, col)


def get_steps_to_coord(paths, wire_id, row, col):
    nsteps = 0
    print('Searching for( ' + str(row) + ', ' + str(col) + ')')
    for wire_row, wire_col in get_all_wire_coords(paths, wire_id):
        nsteps += 1
        print('Found (' + str(wire_row) + ', ' + str(wire_col) + ')')
        if row == wire_row and col == wire_col:
            return nsteps


def day4_part2(paths):
    global crossing_coords

    result = None
    best_cumulative_distance = None
    for crossing_row, crossing_col in crossing_coords:
        cumulative_distance = 0
        for wire_id in range(len(paths)):
            cumulative_distance += get_steps_to_coord(paths, wire_id, crossing_row, crossing_col)
        if result is None or cumulative_distance < best_cumulative_distance:
            result = (crossing_row, crossing_col)
            best_cumulative_distance = cumulative_distance
    return result


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        wire_paths = list(map(lambda path: path.split(','), filter(None, f.read().split('\n'))))
    find_crossings(wire_paths)
    print(shortest_distance)
    print(day4_part2(wire_paths))



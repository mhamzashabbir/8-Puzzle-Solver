def depth_limited_search(state, goal, depth):
    visited = set()
    stack = [(state, [])]
    while stack:
        curr_state, path = stack.pop()
        if curr_state == goal:
            return path
        if len(path) == depth:
            continue
        for move, succ in successors(curr_state):
            if tuple(map(tuple, succ)) in visited:
                continue
            visited.add(tuple(map(tuple, succ)))
            stack.append((succ, path + [move]))
    return None


def iterative_deepening_search(state, goal):
    for depth in range(0, 100):
        result = depth_limited_search(state, goal, depth)
        if result is not None:
            return result
    return None


def successors(state):
    moves = {
        "Up": (-1, 0),
        "Down": (1, 0),
        "Left": (0, -1),
        "Right": (0, 1)
    }

    successors = []
    zero_row, zero_col = find_zero(state)
    for move, (drow, dcol) in moves.items():
        new_row, new_col = zero_row + drow, zero_col + dcol
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = \
                new_state[new_row][new_col], new_state[zero_row][zero_col]
            successors.append((move, new_state))
    return successors


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def count_inversions(state):
    inversions = 0
    tiles = [tile for row in state for tile in row if tile != 0]
    for i, tile in enumerate(tiles):
        for j in range(i + 1, len(tiles)):
            if tiles[j] < tile:
                inversions += 1
    return inversions



state = [[7, 5, 4], [0, 3, 2], [8, 1, 6]]  
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 
inversion = count_inversions(state)
if inversion % 2 == 0:
    print("Solvable")
    solution = iterative_deepening_search(state, goal)
    print(solution)
else:
    print(inversion, "Not Solvable")

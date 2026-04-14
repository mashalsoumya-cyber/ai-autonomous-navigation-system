def get_neighbors(node, rows, cols, obstacles):
    x, y = node
    possible_moves = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    neighbors = []
    for nx, ny in possible_moves:
        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in obstacles:
            neighbors.append((nx, ny))

    return neighbors


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

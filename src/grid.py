import random

ROWS = 20
COLS = 20
CELL_SIZE = 30

START = (1, 1)
GOAL = (18, 18)

def generate_obstacles(count=60):
    obstacles = set()
    while len(obstacles) < count:
        x = random.randint(0, ROWS - 1)
        y = random.randint(0, COLS - 1)

        if (x, y) != START and (x, y) != GOAL:
            obstacles.add((x, y))

    return obstacles

OBSTACLES = generate_obstacles()
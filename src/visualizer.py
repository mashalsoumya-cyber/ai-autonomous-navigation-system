import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
BLUE = (0, 102, 255)
YELLOW = (255, 215, 0)


def draw_grid(screen, rows, cols, cell_size):
    for x in range(rows):
        for y in range(cols):
            rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, rect, 1)


def draw_coordinates(screen, rows, cols, cell_size):
    font = pygame.font.SysFont("Arial", 10)
    for x in range(rows):
        for y in range(cols):
            text = font.render(f"{x},{y}", True, (150, 150, 150))
            screen.blit(text, (y * cell_size + 2, x * cell_size + 2))


def draw_obstacles(screen, obstacles, cell_size):
    for (x, y) in obstacles:
        rect = pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, BLACK, rect)


def draw_start_goal(screen, start, goal, cell_size):
    start_rect = pygame.Rect(
        start[1] * cell_size + 4,
        start[0] * cell_size + 4,
        cell_size - 8,
        cell_size - 8
    )
    goal_rect = pygame.Rect(
        goal[1] * cell_size + 4,
        goal[0] * cell_size + 4,
        cell_size - 8,
        cell_size - 8
    )
    pygame.draw.rect(screen, GREEN, start_rect, border_radius=6)
    pygame.draw.rect(screen, RED, goal_rect, border_radius=6)


def draw_path(screen, path, cell_size):
    if len(path) < 2:
        return

    points = []
    for (x, y) in path:
        center_x = y * cell_size + cell_size // 2
        center_y = x * cell_size + cell_size // 2
        points.append((center_x, center_y))

    pygame.draw.lines(screen, YELLOW, False, points, 4)

    for point in points:
        pygame.draw.circle(screen, YELLOW, point, 4)


def draw_robot(screen, position, cell_size):
    x, y = position
    center_x = y * cell_size + cell_size // 2
    center_y = x * cell_size + cell_size // 2
    pygame.draw.circle(screen, BLUE, (center_x, center_y), cell_size // 3)
import pygame
import time
from src.grid import ROWS, COLS, CELL_SIZE, START, GOAL, OBSTACLES, generate_obstacles
from src.astar import astar
from src.robot import Robot
from src.visualizer import (
    draw_grid,
    draw_obstacles,
    draw_start_goal,
    draw_path,
    draw_robot,
    draw_coordinates
)

pygame.init()

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI-Based Autonomous Navigation System")

font = pygame.font.SysFont("Arial", 20)

# Initial setup
obstacles = OBSTACLES
path = astar(START, GOAL, ROWS, COLS, obstacles)

if not path:
    print("No path found!")
    pygame.quit()
    raise SystemExit

print("Path found:", path)
print("Path length:", len(path))

robot = Robot(path)
clock = pygame.time.Clock()
running = True
last_move_time = time.time()
speed = 0.3

while running:
    screen.fill((255, 255, 255))

    draw_grid(screen, ROWS, COLS, CELL_SIZE)
    draw_coordinates(screen, ROWS, COLS, CELL_SIZE)
    draw_obstacles(screen, obstacles, CELL_SIZE)
    draw_path(screen, path, CELL_SIZE)
    draw_start_goal(screen, START, GOAL, CELL_SIZE)
    draw_robot(screen, robot.get_position(), CELL_SIZE)

    # UI Text
    text = font.render("Autonomous Navigation Running...", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    length_text = font.render(f"Path Length: {len(path)}", True, (0, 0, 0))
    screen.blit(length_text, (10, 40))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # RESET simulation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                obstacles = generate_obstacles()
                path = astar(START, GOAL, ROWS, COLS, obstacles)
                robot = Robot(path)

            # SPEED CONTROL
            if event.key == pygame.K_UP:
                speed = max(0.05, speed - 0.05)

            if event.key == pygame.K_DOWN:
                speed += 0.05

    if time.time() - last_move_time > speed:
        robot.move()
        last_move_time = time.time()

    clock.tick(60)

pygame.quit()
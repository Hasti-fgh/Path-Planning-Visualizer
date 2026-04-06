import numpy as np

EMPTY    = 0
WALL     = 1
START    = 2
END      = 3
EXPLORED = 4
PATH     = 5

ROWS = 30
COLS = 30

def create_grid():
    grid = np.zeros((ROWS, COLS), dtype=int)
    return grid

def set_start(grid, pos):
    grid[pos] = START
    return grid

def set_end(grid, pos):
    grid[pos] = END
    return grid

def add_wall(grid, pos):
    if grid[pos] not in [START, END]:
        grid[pos] = WALL
    return grid

def get_neighbors(grid, node):
    r, c = node
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            if grid[nr][nc] != WALL:
                neighbors.append((nr, nc))
    return neighbors

def reconstruct_path(came_from, start, end):
    path = []
    node = end
    while node != start:
        path.append(node)
        node = came_from[node]
    path.reverse()
    return path
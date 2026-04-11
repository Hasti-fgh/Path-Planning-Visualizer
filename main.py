from src.grid import create_grid, set_start, set_end, add_wall
from src.algorithms import astar, bfs, dijkstra, greedy
from src.visualizer import plot_comparison


def build_hampton():
    g = create_grid()

    # Fill everything with walls
    for r in range(30):
        for c in range(30):
            add_wall(g, (r, c))

    # Carve main correct path (snake)
    for c in range(1, 29): g[1][c] = 0
    for r in range(1, 8):  g[r][28] = 0
    for c in range(6, 29): g[7][c] = 0
    for r in range(7, 14): g[r][6] = 0
    for c in range(6, 29): g[13][c] = 0
    for r in range(13, 20): g[r][28] = 0
    for c in range(6, 29): g[19][c] = 0
    for r in range(19, 26): g[r][6] = 0
    for c in range(6, 29): g[25][c] = 0
    for r in range(25, 29): g[r][28] = 0
    g[28][28] = 0

    # Dead end 1 - long decoy going LEFT from row 1
    for c in range(1, 20): g[3][c] = 0
    for r in range(1, 4):  g[r][1] = 0

    # Dead end 2 - decoy corridor off row 7
    for c in range(1, 6):  g[7][c] = 0
    for r in range(7, 14): g[r][1] = 0
    for c in range(1, 6):  g[13][c] = 0

    # Dead end 3 - long decoy off row 13
    for c in range(1, 6):  g[10][c] = 0
    for r in range(8, 11): g[r][5] = 0

    # Dead end 4 - decoy going up from row 19
    for c in range(1, 6):  g[19][c] = 0
    for r in range(15, 20): g[r][2] = 0
    for c in range(2, 6):   g[15][c] = 0

    # Dead end 5 - decoy off row 25
    for c in range(1, 6):  g[25][c] = 0
    for r in range(20, 26): g[r][1] = 0
    for c in range(1, 4):   g[20][c] = 0

    # Dead end 6 - mid maze confusion
    for r in range(1, 7):  g[r][15] = 0
    for c in range(10, 16): g[6][c] = 0
    for r in range(6, 13): g[r][10] = 0
    for c in range(10, 16): g[12][c] = 0

    g[1][1] = 0
    g[28][28] = 0
    set_start(g, (1, 1))
    set_end(g, (28, 28))
    return g


if __name__ == '__main__':
    print("Running A*...")
    g1 = build_hampton()
    e1, p1 = astar(g1, (1, 1), (28, 28))
    print(f"A*:       {len(p1)} steps | {len(e1)} cells explored")

    print("Running BFS...")
    g2 = build_hampton()
    e2, p2 = bfs(g2, (1, 1), (28, 28))
    print(f"BFS:      {len(p2)} steps | {len(e2)} cells explored")

    print("Running Dijkstra...")
    g3 = build_hampton()
    e3, p3 = dijkstra(g3, (1, 1), (28, 28))
    print(f"Dijkstra: {len(p3)} steps | {len(e3)} cells explored")

    print("Running Greedy...")
    g4 = build_hampton()
    e4, p4 = greedy(g4, (1, 1), (28, 28))
    print(f"Greedy:   {len(p4)} steps | {len(e4)} cells explored")

    results = [
        (g1, e1, p1, f"A*\nPath: {len(p1)} steps | Explored: {len(e1)} cells"),
        (g2, e2, p2, f"BFS\nPath: {len(p2)} steps | Explored: {len(e2)} cells"),
        (g3, e3, p3, f"Dijkstra\nPath: {len(p3)} steps | Explored: {len(e3)} cells"),
        (g4, e4, p4, f"Greedy\nPath: {len(p4)} steps | Explored: {len(e4)} cells"),
    ]
    plot_comparison(results, "Hampton Court Palace Maze — Algorithm Comparison",
                    "demo/algorithm_comparison.png")

from src.grid import create_grid, set_start, set_end, add_wall
from src.algorithms import astar, bfs, dijkstra
from src.visualizer import plot_comparison


def build_hampton():
    g = create_grid()
    for r in range(30):
        for c in range(30):
            add_wall(g, (r, c))
    for c in range(1, 29): g[1][c] = 0
    for r in range(1, 6):  g[r][28] = 0
    for c in range(4, 29): g[5][c] = 0
    for r in range(5, 11): g[r][4] = 0
    for c in range(4, 28): g[10][c] = 0
    for r in range(10, 16): g[r][27] = 0
    for c in range(3, 28): g[15][c] = 0
    for r in range(15, 21): g[r][3] = 0
    for c in range(3, 28): g[20][c] = 0
    for r in range(20, 26): g[r][27] = 0
    for c in range(3, 28): g[25][c] = 0
    for r in range(25, 28): g[r][3] = 0
    for c in range(3, 28): g[27][c] = 0
    g[1][1] = 0
    g[27][27] = 0
    set_start(g, (1, 1))
    set_end(g, (27, 27))
    return g


if __name__ == '__main__':
    print("Running A*...")
    g1 = build_hampton()
    e1, p1 = astar(g1, (1, 1), (27, 27))
    print(f"A*:       {len(p1)} steps | {len(e1)} cells explored")

    print("Running BFS...")
    g2 = build_hampton()
    e2, p2 = bfs(g2, (1, 1), (27, 27))
    print(f"BFS:      {len(p2)} steps | {len(e2)} cells explored")

    print("Running Dijkstra...")
    g3 = build_hampton()
    e3, p3 = dijkstra(g3, (1, 1), (27, 27))
    print(f"Dijkstra: {len(p3)} steps | {len(e3)} cells explored")

    results = [
        (g1, e1, p1, f"A*\nPath: {len(p1)} steps | Explored: {len(e1)} cells"),
        (g2, e2, p2, f"BFS\nPath: {len(p2)} steps | Explored: {len(e2)} cells"),
        (g3, e3, p3, f"Dijkstra\nPath: {len(p3)} steps | Explored: {len(e3)} cells"),
    ]
    plot_comparison(results, "Hampton Court Palace Maze — Algorithm Comparison",
                    "demo/algorithm_comparison.png")

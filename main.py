import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from src.grid import create_grid, set_start, set_end, add_wall
from src.algorithms import astar, bfs, dijkstra

COLORS = mcolors.ListedColormap([
    'white', '#2C2C2A', '#1D9E75', '#D85A30', '#B5D4F4', '#FAC775'
])

def build_result(grid, explored, path):
    display = grid.copy()
    for r, c in explored:
        if display[r][c] == 0:
            display[r][c] = 4
    if path:
        for r, c in path:
            if display[r][c] not in [2, 3]:
                display[r][c] = 5
    return display

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
    set_start(g, (1,1))
    set_end(g, (27,27))
    return g

# --- Run all 3 algorithms on Hampton Court ---
print("Running A*...")
g1 = build_hampton()
e1, p1 = astar(g1, (1,1), (27,27))
print(f"A*: {len(p1)} steps, {len(e1)} explored")

print("Running BFS...")
g2 = build_hampton()
e2, p2 = bfs(g2, (1,1), (27,27))
print(f"BFS: {len(p2)} steps, {len(e2)} explored")

print("Running Dijkstra...")
g3 = build_hampton()
e3, p3 = dijkstra(g3, (1,1), (27,27))
print(f"Dijkstra: {len(p3)} steps, {len(e3)} explored")

# --- Plot ---
fig, axes = plt.subplots(1, 3, figsize=(22, 8))

data = [
    (g1, e1, p1, f"A*\nPath: {len(p1)} steps | Explored: {len(e1)} cells"),
    (g2, e2, p2, f"BFS\nPath: {len(p2)} steps | Explored: {len(e2)} cells"),
    (g3, e3, p3, f"Dijkstra\nPath: {len(p3)} steps | Explored: {len(e3)} cells"),
]

for ax, (g, e, p, title) in zip(axes, data):
    display = build_result(g, e, p)
    ax.imshow(display, cmap=COLORS, vmin=0, vmax=5)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    ax.axis('off')

plt.suptitle("Hampton Court Palace Maze — Algorithm Comparison", 
             fontsize=15, fontweight='bold', y=1.02)

# Legend
from matplotlib.patches import Patch
legend = [
    Patch(color='#1D9E75', label='Start'),
    Patch(color='#D85A30', label='End'),
    Patch(color='#B5D4F4', label='Explored'),
    Patch(color='#FAC775', label='Path'),
    Patch(color='#2C2C2A', label='Wall'),
]
fig.legend(handles=legend, loc='lower center', ncol=5, 
           fontsize=11, frameon=False, bbox_to_anchor=(0.5, -0.05))

plt.tight_layout()
plt.savefig("demo/algorithm_comparison.png", dpi=150, bbox_inches='tight')
print("✅ Saved to demo/algorithm_comparison.png")
plt.show()
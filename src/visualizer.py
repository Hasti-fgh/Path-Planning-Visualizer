import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
from matplotlib.patches import Patch
from src.grid import EMPTY, START, END, EXPLORED, PATH

COLORS = mcolors.ListedColormap([
    'white',
    '#2C2C2A',
    '#1D9E75',
    '#D85A30',
    '#B5D4F4',
    '#FAC775'
])


def build_result(grid, explored, path):
    display = grid.copy()
    for r, c in explored:
        if display[r][c] == EMPTY:
            display[r][c] = EXPLORED
    if path:
        for r, c in path:
            if display[r][c] not in [START, END]:
                display[r][c] = PATH
    return display


def plot_comparison(results, suptitle, save_path):
    """results: list of (grid, explored, path, label) tuples"""
    fig, axes = plt.subplots(1, len(results), figsize=(22, 8))
    if len(results) == 1:
        axes = [axes]

    for ax, (g, e, p, label) in zip(axes, results):
        display = build_result(g, e, p)
        ax.imshow(display, cmap=COLORS, vmin=0, vmax=5)
        ax.set_title(label, fontsize=12, fontweight='bold', pad=10)
        ax.axis('off')

    plt.suptitle(suptitle, fontsize=15, fontweight='bold', y=1.02)

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
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"Saved to {save_path}")
    plt.show()

def animate(grid, explored, path, title='Path Planning'):
    fig, ax = plt.subplots(figsize=(8, 8))
    display = grid.copy()
    total_frames = len(explored) + (len(path) if path else 0)

    def update(frame):
        if frame < len(explored):
            r, c = explored[frame]
            if display[r][c] == EMPTY:
                display[r][c] = EXPLORED
        elif path:
            idx = frame - len(explored)
            if idx < len(path):
                r, c = path[idx]
                if display[r][c] not in [START, END]:
                    display[r][c] = PATH
        ax.clear()
        ax.imshow(display, cmap=COLORS, vmin=0, vmax=5)
        ax.set_title(title, fontsize=14)
        ax.axis('off')

    ani = animation.FuncAnimation(
        fig, update,
        frames=total_frames,
        interval=50,
        repeat=False
    )
    plt.tight_layout()
    plt.show()
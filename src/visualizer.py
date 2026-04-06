import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as animation
from src.grid import EMPTY, START, END, EXPLORED, PATH

COLORS = mcolors.ListedColormap([
    'white',
    '#2C2C2A',
    '#1D9E75',
    '#D85A30',
    '#B5D4F4',
    '#FAC775'
])

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
# Path Planning Visualizer

A visual comparison of three classic pathfinding algorithms — A*, BFS, and Dijkstra — navigating a maze inspired by the **Hampton Court Palace Maze** in Surrey, UK. Hampton Court's hedge maze is one of the oldest and most famous labyrinths in England, known for its winding dead ends and deceptive corridors that have been confusing visitors since the 1690s.

![Algorithm Comparison](demo/algorithm_comparison.png)

## Algorithms

| Algorithm | Strategy | Optimal Path | Notes |
|-----------|----------|-------------|-------|
| **A\*** | Heuristic-guided (Manhattan distance) | Yes | Explores fewer cells by estimating distance to goal |
| **BFS** | Level-by-level exploration | Yes (unweighted) | Guarantees shortest path, explores broadly |
| **Dijkstra** | Lowest-cost first | Yes | Equivalent to BFS on uniform-cost grids |

## Project Structure

```
├── main.py              # Hampton Court-inspired maze
├── run_all.py           # Custom maze with deliberate dead ends
├── src/
│   ├── grid.py          # Grid creation, neighbors, path reconstruction
│   ├── algorithms.py    # A*, BFS, Dijkstra implementations
│   └── visualizer.py    # Side-by-side plot + animation support
├── demo/
│   └── algorithm_comparison.png
└── requirements.txt
```

## Getting Started

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the Hampton Court maze:**
```bash
python main.py
```

**Run the custom maze:**
```bash
python run_all.py
```

Both scripts print step counts to the terminal and save a comparison image to `demo/algorithm_comparison.png`.

## Colour Legend

| Colour | Meaning |
|--------|---------|
| White | Open path |
| Dark | Wall |
| Green | Start |
| Orange | End |
| Light blue | Explored cells |
| Yellow | Final path |

## Requirements

- Python 3.8+
- numpy
- matplotlib

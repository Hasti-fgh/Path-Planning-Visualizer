from collections import deque
import heapq
from src.grid import get_neighbors, reconstruct_path

def bfs(grid, start, end):
    queue = deque([start])
    came_from = {start: None}
    explored = []

    while queue:
        current = queue.popleft()
        explored.append(current)

        if current == end:
            return explored, reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(grid, current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                queue.append(neighbor)

    return explored, None


def dijkstra(grid, start, end):
    heap = [(0, start)]
    came_from = {start: None}
    cost = {start: 0}
    explored = []

    while heap:
        curr_cost, current = heapq.heappop(heap)
        explored.append(current)

        if current == end:
            return explored, reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(grid, current):
            new_cost = cost[current] + 1
            if new_cost < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(heap, (new_cost, neighbor))

    return explored, None


def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(grid, start, end):
    heap = [(0, start)]
    came_from = {start: None}
    g_score = {start: 0}
    explored = []

    while heap:
        _, current = heapq.heappop(heap)
        explored.append(current)

        if current == end:
            return explored, reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(grid, current):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, end)
                heapq.heappush(heap, (f, neighbor))

    return explored, None


def greedy(grid, start, end):
    heap = [(heuristic(start, end), start)]
    came_from = {start: None}
    explored = []

    while heap:
        _, current = heapq.heappop(heap)
        explored.append(current)

        if current == end:
            return explored, reconstruct_path(came_from, start, end)

        for neighbor in get_neighbors(grid, current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(heap, (heuristic(neighbor, end), neighbor))

    return explored, None
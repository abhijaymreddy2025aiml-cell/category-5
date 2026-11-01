
import heapq

def greedy_bfs(graph, heuristic, start, goal):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor], neighbor,
                     path + [neighbor])
                )

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 3,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

result = greedy_bfs(graph, heuristic, start, goal)

if result:
    print("Path found:", " -> ".join(result))
else:
    print("Goal not found")

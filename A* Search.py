
import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start, [start])]
    visited = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in visited and visited[node] <= g:
            continue

        visited[node] = g

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]

            if neighbor not in visited or new_g < visited[neighbor]:
                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor,
                     path + [neighbor])
                )

    return None, float('inf')


# Weighted graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}

start = 'A'
goal = 'G'

path, cost = astar(graph, heuristic, start, goal)

if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Goal not found")

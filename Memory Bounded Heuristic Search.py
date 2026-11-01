
def rbfs(graph, heuristic, node, goal,
         g, f, f_limit, path):

    if node == goal:
        return path, g

    successors = []

    for neighbor, cost in graph[node]:
        if neighbor not in path:
            new_g = g + cost
            new_f = max(
                new_g + heuristic[neighbor],
                f
            )

            successors.append(
                [neighbor, new_g, new_f]
            )

    if not successors:
        return None, float('inf')

    while True:
        successors.sort(key=lambda x: x[2])

        best = successors[0]

        if best[2] > f_limit:
            return None, best[2]

        if len(successors) > 1:
            alternative = successors[1][2]
        else:
            alternative = float('inf')

        result, new_f = rbfs(
            graph,
            heuristic,
            best[0],
            goal,
            best[1],
            best[2],
            min(f_limit, alternative),
            path + [best[0]]
        )

        best[2] = new_f

        if result:
            return result, new_f


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

path, cost = rbfs(
    graph, heuristic,
    start, goal,
    0, heuristic[start],
    float('inf'), [start]
)

if path:
    print("Path Found:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Goal not found")

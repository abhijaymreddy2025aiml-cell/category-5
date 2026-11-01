
def ao_star(graph, heuristic, node, solution, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        raise ValueError("Cycle detected in graph")

    # Terminal node
    if node not in graph or not graph[node]:
        return heuristic[node]

    visited.add(node)

    min_cost = float('inf')
    best_option = None

    # Each option represents an AND group.
    # Different options represent OR choices.
    for option in graph[node]:
        cost = 0

        for child, edge_cost in option:
            cost += edge_cost + ao_star(
                graph, heuristic, child,
                solution, visited.copy()
            )

        if cost < min_cost:
            min_cost = cost
            best_option = option

    solution[node] = [child for child, cost in best_option]

    return min_cost


# AND-OR graph
graph = {
    'S': [
        [('A', 1), ('B', 1)],
        [('C', 2)]
    ],
    'A': [[('D', 2)]],
    'B': [[('E', 2)]],
    'C': [[('F', 1), ('G', 1)]],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

heuristic = {
    'S': 5,
    'A': 3,
    'B': 3,
    'C': 2,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0
}

solution = {}

cost = ao_star(graph, heuristic, 'S', solution)

print("Minimum Cost:", cost)
print("Solution Graph:")

for node, children in solution.items():
    print(node, "->", children)

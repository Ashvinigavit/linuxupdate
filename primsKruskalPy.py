def kruskal(graph):
    minimum_spanning_tree = []
    graph.sort(key=lambda edge: edge[2])  # Sort edges by distance
    parent = {city: city for city in graph.keys()}

    for city1, city2, distance in graph:
        if find(parent, city1) != find(parent, city2):
            minimum_spanning_tree.append((city1, city2, distance))
            union(parent, city1, city2)

    return minimum_spanning_tree

def prims(graph):
    visited = {city: False for city in graph.keys()}
    minimum_spanning_tree = []
    visited[list(graph.keys())[0]] = True

    while len(minimum_spanning_tree) < len(graph) - 1:
        min_distance = float('inf')
        min_edge = None
        for city1 in graph:
            if visited[city1]:
                for city2, distance in graph[city1].items():
                    if not visited[city2] and distance < min_distance:
                        min_distance = distance
                        min_edge = (city1, city2, distance)
        city1, city2, distance = min_edge
        minimum_spanning_tree.append((city1, city2, distance))
        visited[city2] = True

    return minimum_spanning_tree

# Example usage
city_graph = {
    'A': {'B': 2, 'D': 6},
    'B': {'A': 2, 'C': 3, 'E': 8, 'D': 5},
    'C': {'B': 3, 'E': 7},
    'D': {'A': 6, 'B': 5, 'E': 9},
    'E': {'B': 8, 'C': 7, 'D': 9}
}

kruskal_result = kruskal([(city1, city2, distance) for city1, connections in city_graph.items() for city2, distance in connections.items()])
prims_result = prims(city_graph)

print("Kruskal's Algorithm:")
for edge in kruskal_result:
    print(edge)

print("\nPrim's Algorithm:")
for edge in prims_result:
    print(edge)

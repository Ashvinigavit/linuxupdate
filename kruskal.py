def find(parent, city):
    if parent[city] != city:
        parent[city] = find(parent, parent[city])
    return parent[city]

def union(parent, rank, city1, city2):
    root1 = find(parent, city1)
    root2 = find(parent, city2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

def kruskal(graph):
    minimum_spanning_tree = []
    edges = [(city1, city2, distance) for city1 in graph for city2, distance in graph[city1]]
    edges.sort(key=lambda edge: edge[2])  # Sort edges by distance
    parent = {city: city for city in graph}
    rank = {city: 0 for city in graph}

    for city1, city2, distance in edges:
        if find(parent, city1) != find(parent, city2):
            minimum_spanning_tree.append((city1, city2, distance))
            union(parent, rank, city1, city2)

    return minimum_spanning_tree

# Example usage
city_graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('E', 8), ('D', 5)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 5), ('E', 9)],
    'E': [('B', 8), ('C', 7), ('D', 9)]
}

kruskal_result = kruskal(city_graph)

print("Kruskal's Algorithm:")
for edge in kruskal_result:
    print(edge)

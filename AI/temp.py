graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'G'],
    'F': ['C', 'H'],
    'G': ['D', 'E', 'I'],
    'H': ['F', 'I'],
    'I': ['H', 'G']
}

visited = []
queue = []

def bfs(graph, node):
    queue.append(node)
    visited.append(node)
    
    while queue:
        m = queue.pop(0)
        print(m)

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS")
bfs(graph, "A")
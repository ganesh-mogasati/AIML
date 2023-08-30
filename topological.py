from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

num_vertices = int(input())
num_edges = int(input())
graph = defaultdict(list)

for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start_vertex = int(input())
bfs(graph, start_vertex)

def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

num_vertices = int(input())
num_edges = int(input())
graph = {}
for i in range(num_vertices):
    graph[i] = []

for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start_vertex = int(input())
visited = set()
dfs(graph, start_vertex, visited)


def topological_sort(graph):
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(vertex)

    visited = set()
    result = []

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return result[::-1]

num_vertices = int(input())
num_edges = int(input())

graph = {}
for i in range(1, num_vertices + 1):
    graph[i] = []

for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)

topological_order = topological_sort(graph)
print("Topological sorting:", topological_order)
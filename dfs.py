def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph={
    0:[1,2],
    1:[2,3],
    2:[4],
    3:[],
    4:[]
}
start_vertex = int(input())
visited = set()
dfs(graph, start_vertex, visited)          

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

a=int(input())
for i in range (a//a,a):
    print(i)
print(a)



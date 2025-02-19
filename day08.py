def dfs(g, i, visited):
    visited[i] = 1
	print(visited)
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]: # 연결이 되어 있으면서 동시에 방문한 적이 없는
            dfs(g, j, visited)

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

visited = [0] * len(graph)
dfs(graph, 0, visited)

"""
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 1] E
[0, 0, 1, 0, 1] C
[1, 0, 1, 0, 1] A
[1, 0, 1, 1, 1] D
D -> A -> C 
[1, 1, 1, 1, 1] B
B -> C
"""

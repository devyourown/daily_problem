from collections import deque

N, M, start = map(int, input().split())

graph = [[] for _ in range(N+1)]
isvisited = [False for _ in range(N+1)]

for _ in range(M):
    index, V = map(int, input().split())
    graph[index].append(V)
    graph[V].append(index)

for i in range(1, N+1):
    graph[i].sort()


def dfs(start):
    isvisited[start] = True
    print(start, end=" ")
    for node in graph[start]:
        if not isvisited[node]:
            dfs(node)

def bfs(start):
    q = deque();

    q.append(start)
    isvisited[start] = True
    print(start, end=" ")
    while q:
        index = q.popleft()
        for node in graph[index]:
            if not isvisited[node]:
                isvisited[node] = True
                print(node, end=" ")
                q.append(node)

dfs(start)
isvisited = [False for _ in range(N+1)]
print()
bfs(start)
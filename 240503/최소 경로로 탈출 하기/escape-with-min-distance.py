import sys
from collections import deque
input =sys.stdin.readline
n,m = map(int,input().split())
graph = []
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
ans = -1
visited = [ [False]*(m) for _ in range(n)]
queue = deque()

def in_range(x,y):
    return 0<= x <n and 0<= y < m

def push(x,y,s):
    if graph[x][y] == 1:
        graph[x][y] = s
        visited[x][y] = True
        queue.append([x,y])


def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if in_range(new_x, new_y) and not visited[new_x][new_y] and graph[new_x][new_y] == 1:
                push(new_x,new_y, graph[x][y] + 1)

push(0,0,0)
bfs()
if visited[n-1][m-1]:
    print(graph[n-1][m-1])
else:
    print(-1)
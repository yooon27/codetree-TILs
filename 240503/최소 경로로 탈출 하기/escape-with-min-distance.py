import sys
from collections import deque
input =sys.stdin.readline
n,m = map(int,input().split())
graph = []
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
ans = -1
visited = [[-1]*(n) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(r,c,cost):
    queue = deque()
    queue.append([r,c])
    visited[r][c] = cost
    past_cost = cost
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            
            now_x = x + dx[i]
            now_y = y + dy[i]
            if 0<= now_x < n and 0<= now_y < n:
                if visited[now_x][now_y] < 0 and graph[now_x][now_y] == 1:
                    past_cost = 100
                    for j in range(4):
                        nn_x = now_x + dx[j]
                        nn_y = now_y + dy[j]
                        if 0<= nn_x < n and 0<= nn_y < n:

                            if visited[nn_x][nn_y] != -1 and past_cost > visited[nn_x][nn_y]:
                                past_cost = visited[nn_x][nn_y]
                    
                    visited[now_x][now_y] = past_cost+1
                    queue.append([now_x,now_y])

bfs(0,0,0)

print(visited[n-1][n-1])
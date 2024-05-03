import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

dp = [[0]*n for _ in range(n)]

# first initialization
for i in range(n):
    dp[0][i] += graph[0][i]
for j in range(n):
    dp[j][n-1] += graph[j][n-1]

#second initialization(right and down)
for i in range(n):
    dp[i][0] += graph[i][0]
for j in range(n):
    dp[n-1][j] += graph[n-1][j]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + graph[i][j] , dp[i][j-1] + graph[i][j])

print(dp[n-1][n-1])
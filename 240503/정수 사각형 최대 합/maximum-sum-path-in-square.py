import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

dp = [[0]*n for _ in range(n)]

dp[0][0] = graph[0][0]

# first initialization
if n > 1:
    for i in range(1,n):
        dp[0][i] += graph[0][i] + dp[0][i-1]
    for j in range(1,n):
        dp[j][n-1] += graph[j][n-1] + dp[j-1][n-1]

    #second initialization(right and down)
    for i in range(1,n):
        dp[i][0] += graph[i][0] + dp[i-1][0]
    for j in range(1,n):
        dp[n-1][j] += graph[n-1][j] + dp[n-1][j-1]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j] + graph[i][j] , dp[i][j-1] + graph[i][j])

print(dp[n-1][n-1])
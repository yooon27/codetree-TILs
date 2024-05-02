import sys
input = sys.stdin.readline
n = int(input())

ans = 0
arr = [0]*1001

arr[0] = 0
arr[2] = 1
arr[3] = 1

for i in range(4, n+1):
    arr[i] = arr[i-2] + arr[i-3]

print(arr[n]%10007)
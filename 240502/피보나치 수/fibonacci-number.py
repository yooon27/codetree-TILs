import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 46

arr[1] = 1
arr[2] = 1

def fibbo(n):
    if arr[n] != 0:
        return arr[n]
    
    arr[n] = fibbo(n-1) + fibbo(n-2)
    return arr[n]

if n <= 2:
    print(1)
else:
    print(fibbo(n))
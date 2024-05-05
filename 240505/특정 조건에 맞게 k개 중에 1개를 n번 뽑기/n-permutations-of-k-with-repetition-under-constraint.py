import sys
input = sys.stdin.readline

K, N = map(int,input().split())
arr = []

def print_sentence():
    count = 1
    past_num = 0
    for i in range(N):
        if arr[i] == past_num:
            count += 1
        else:
            count = 1
        past_num = arr[i]
        if count == 3:
            return
    
    for i in range(N):
        print(arr[i], end = ' ')
    print()

def backtracking_basic():
    if len(arr) == N:
        print_sentence()
        return
    
    for i in range(1,K+1):

        arr.append(i)
        backtracking_basic()
        arr.pop()
    
    return

backtracking_basic()
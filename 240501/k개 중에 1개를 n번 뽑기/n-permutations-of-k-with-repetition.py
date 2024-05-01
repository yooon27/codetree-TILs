k, n = map(int,input().split())

def p_str(sentence):
    for i in range(n):
        print(sentence[i],end=' ')
        
    print()

arr = []
def function(num):
    if num == n+1:
        p_str(arr)
        return
    for i in range(1,k+1):
        arr.append(i)
        function(num+1)
        arr.pop()
    
function(1)
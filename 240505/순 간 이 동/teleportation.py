import sys
input =sys.stdin.readline
a, b, x, y = map(int,input().split())
if a > b:
    a,b = b, a
if x > y:
    x,y= y,x

# case 1 
minimum = b-a

# case 2 => x => a and b => y
minimum = min(minimum, (abs(x-a)+abs(b-y)))

# case 3 => x => b and a => y
minimum = min(minimum, (abs(x-b)+abs(a-y)))

print(minimum)
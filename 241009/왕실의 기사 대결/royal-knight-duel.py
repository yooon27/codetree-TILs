import sys
input = sys.stdin.readline
from collections import deque

MAX_N = 31
MAX_L = 41
dx = [-1,0,1,0]
dy = [0,1,0,-1]

info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)] #전체 체스판 최대 크기 세팅
bef_k = [0 for _ in range(MAX_N)] # 최대 기사들에 대한 각 기사별 체력 정보
r = [0 for _ in range(MAX_N)] # 초기 기사 정보 중 r (초기 위치)
c = [0 for _ in range(MAX_N)] # 초기 기사 정보 중 c (초기 위치)
h = [0 for _ in range(MAX_N)] # 초기 기사 정보 중 h (기사 크기)
w = [0 for _ in range(MAX_N)] # 초기 기사 정보 중 w (기사 크기)
k = [0 for _ in range(MAX_N)] # 기사 체력 현황
nr = [0 for _ in range(MAX_N)] # 기사들의 현재 위치 정보
nc = [0 for _ in range(MAX_N)] # 기사들의 현재 위치 정보
dmg = [0 for _ in range(MAX_N)] # 기사별 데미지를 받은 정보 저장 공간
is_moved = [False for _ in range(MAX_N)] 

# 기사의 움직임을 시도하는 함수
def try_movement(idx , dir):
    q = deque()
    is_pos = True

    # 초기화 (1번부터 n번까지의 기사들의 정보 [데미지 , 움직일 수 있는지 , 현재 위치])
    for i in range(1, n+1):
        dmg[i] = 0
        is_moved[i] = False
        nr[i] = r[i]
        nc[i] = c[i]
    
    q.append(idx) # 왕실 명령을 받아 움직여야하는 기사의 번호를 idx 로 이를 q에 넣음
    is_moved[idx] = True # 해당 기사는 움직일 것이므로 True로 표기

    while q:
        x = q.popleft() #이번에 움직여야할 기사
        

        nr[x] += dx[dir]
        nc[x] += dy[dir]

        # 체스판 자체를 벗어나는지 체크
        if nr[x] < 1 or nc[x] < 1 or nr[x]+h[x] - 1 > l or nc[x] + w[x] - 1 > l:
            return False
        
        # 기사가 다른 기사나 벽에 충돌하는지 체크
        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:
                    dmg[x] += 1 # 해당 위치가 함정이 있다면 데미지 추가
                if info[i][j] == 2:
                    return False # 해당 위치에 벽이 있다면 움직일 ㅅ 없음


        
        # 충돌한 기사가 움질일 경우 충돌되는 기사의 움직임 확인
        for i in range(1,n+1):
            # 기사 중에 이미 한 번 움직인 사람이 있거나, 체력이 0 이하이면 건너뛰기
            if is_moved[i] or k[i] <= 0 : 
                continue
            # 현재 움직이는 기사가 나머지 기사들에게 충돌이 되는지 확인하여 인접하지 않으면 건너뛰기
            if r[i] > nr[x] + h[x] - 1 or nr[x] > r[i] + h[i] - 1:
                continue
            if c[i] > nc[x] + w[x] - 1 or nc[x] > c[i] + w[i] - 1:
                continue
            
            is_moved[i] = True
            q.append(i)
        
    # 명령을 받은 기사는 데미지가 축적되지 않으니 데미지 초기화
    dmg[idx] = 0
    return True

# 특정 조각을 지정된 방향으로 이동
def move_piece(idx, move_dir):
    # 체력 없으면 x
    if k[idx] <= 0 :
        return
    
    # 이동이 가능하다면 , 실제 위치랑 체력을 업데이트
    if try_movement(idx, move_dir):
        for i in range(1,n+1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]




# 입력값 (L, N, Q)
l , n , q = map(int, input().split())
for i in range(1, l+1):
    info[i][1:] = map(int, input().split())
for i in range(1,n+1):
    r[i], c[i] , h[i] , w[i], k[i] = map(int,input().split())
    bef_k[i] = k[i]

for _ in range(q):
    idx, d = map(int,input().split())
    move_piece(idx, d)

# 결과 계산
ans = 0
for i in range(1,n+1):
    if k[i] > 0:
        ans += bef_k[i] - k[i]
        

print(ans)
import sys
input = sys.stdin.readline

MAX_N = 100001
MAX_D = 22

# 변수 세팅
n, q = 0, 0
a = [0] * MAX_N #authority (권한)정보
p = [0] * MAX_N #parent 노드 정보
val = [0] * MAX_N 
noti = [False] * MAX_N
nx = [[0 for _ in range(MAX_D)] for _ in range(MAX_N)]

# 초기 설정 값을 받기
def init(inputs):
    global n, a, p, val, nx
    # parent 채팅과 채팅의 권한 정보에 대한 입력
    for i in range(1,n+1):
        p[i] = inputs[i]
    
    for i in range(1,n+1):
        a[i] = inputs[i+n]
        # 채팅의 권한이 20을 초과한다면 20으로 제한
        if a[i] > 20:
            a[i] = 20

    # nx 배열하고 val 값을 초기화
    for i in range(1, n+1):
        cur = i # 현재 노드
        x = a[i] # 현재 노드에 대한 권한 정도를 x
        nx[cur][x] += 1 #cur번 채팅창의 권한이 x일 때 알림의 수
        # 상위 채팅으로 이동하면서 nx와 val값을 갱신

        while p[cur] and x:
            cur = p[cur]
            x -= 1
            if x:
                nx[cur][x] += 1
            val[cur] += 1 # cur번 채팅창이 권한에 상관없이 받은 알림의 전체 수

# 채팅의 알림 상태 toggle
def toggle_noti(chat):
    cur = p[chat]
    num = 1

    # 상위 채팅으로 이동하면서 noti 값에 따라서 nx와 val 값을 갱신
    while cur:
        for i in range(num, 22):
            if noti[chat]:
                val[cur] += nx[chat][i]
            else:
                val[cur] -= nx[chat][i]

            if i > num:
                if noti[chat]:
                    nx[cur][i-num] += nx[chat][i]
                else:
                    nx[cur][i-num] -= nx[chat][i]
        if noti[cur]:
            break
        cur = p[cur]
        num += 1
    noti[chat] = not noti[chat]


# 채팅의 권한의 크기를 변경 : 300
def change_power(chat, power):
    bef_power = a[chat]
    power = min(power, 20)
    a[chat] = power

    nx[chat][bef_power] -= 1
    if not noti[chat]:
        cur = p[chat]
        num = 1
        # 상위 채팅으로 이동하면서 nx , val 값을 갱신
        while cur:
            if bef_power >= num:
                val[cur] -= 1
            if bef_power > num:
                nx[cur][bef_power - num] -= 1
            if noti[cur]:
                break
            cur = p[cur]
            num += 1
    
    nx[chat][power] += 1
    if not noti[chat]:
        cur = p[chat]
        num = 1
        # 상위 채팅으로 이동하면서 nx, val 값 갱신
        while cur:
            if power >= num:
                val[cur] += 1
                if power > num:
                    nx[cur][power - num] += 1
                if noti[cur]:
                    break
                cur = p[cur]
                num += 1


# 두 채팅의 부모 노드를 교체 400
def change_parent(chat1, chat2):
    bef_noti1 = noti[chat1]
    bef_noti2 = noti[chat2]

    if not noti[chat1]:
        toggle_noti(chat1)
    if not noti[chat2]:
        toggle_noti(chat2)
    
    p[chat1] , p[chat2] = p[chat2] , p[chat1]

    if not bef_noti1:
        toggle_noti(chat1)
    if not bef_noti2:
        toggle_noti(chat2)


# 해당 채팅의 val (알림 수) 를 출력
def print_count(chat):
    print(val[chat])



n, q = map(int,input().split())
for _ in range(q):
    inputs = list(map(int,input().split()))
    query = inputs[0]
    if query == 100:
        init(inputs)
    elif query == 200:
        chat = inputs[1]
        toggle_noti(chat)
    elif query == 300:
        chat, power = inputs[1], inputs[2]
        change_power(chat, power)
    elif query == 400:
        chat1, chat2 = inputs[1], inputs[2]
        change_parent(chat1, chat2)
    elif query == 500:
        chat = inputs[1]
        print_count(chat)
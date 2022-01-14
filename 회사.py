INF = int(1e9) # 무한의 값으로 10억을 설정
n,m = map(int,input().split()) # 노드, 간선의 갯수 입력
gra = [[INF] * (n+1) for _ in range(n+1)] # 2차원 테이블  초기화

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b: # 자기자신에서 자기자신으로 가는비용
            gra[a][b] = 0 # 0으로 만든다

for i in range(m):
    a,b = map(int,input().split()) # 간선에 대한 정보를 입력
    gra[a][b] = 1 # a-->b 1
    gra[b][a] = 1 # b-->a 1

k, x = map(int,input().split()) # 거쳐갈 노드 k와 최종 목적지 x 입력받기

for x in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            gra[a][b] = min(gra[a][b], gra[a][x]+gra[x][b])

dist = gra[1][x] + gra[x][k]

if dist >= INF: # 도달할 수 없는 경우
    print("-1")
else: # 도달할 수 있는 경우
    print(dist)
INF = int(1e9)

n = int(input()) # 도시의 갯수 입력
m = int(input()) # 버스의 갯수 입력

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 테이블 초기화

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b: # 자기자신에서 자기자신으로 가는 비용
            graph[a][b] = 0 # 0으로 초기화

for i in range(m):
    a,b,c = map(int,input().split()) # a도시에서 b도시까지 가는 비용 c

    if c < graph[a][b]: # 가장 짧은 정보만을 저장
        graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# 결과출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF: # 도달할 수 없는 경우
            print(0, end=' ') # 0을 출력
        else: # 도달할 수 있는 경우
            print(graph[a][b])
    print()
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n,m = map(int, input().split()) # n = 노드의 갯수 입력 , m = 간선의 갯수 입력

graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원리스트를 만들고 무한대의 값으로 초기화

# 자기자신에서 자기자신으로 가는 경우에는 0으로 초기화

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int,input().split()) # 각 간선에 대한 정보를 입력받는다
    graph[a][b] = 1 # 간선에 대한 정보를 1로 초기화
    graph[b][a] = 1

x,k = map(int, input().split()) # x = 거쳐갈 노드 , k = 최종 목적지 노드 입력받기

# 플로이드 워셜 알고리즘

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력

distance = graph[1][k] + graph[k][x]

if distance >= INF: # 도달할 수 없는 경우
    print("-1")

else: # 도달할 수 있는 경우
    print(distance)
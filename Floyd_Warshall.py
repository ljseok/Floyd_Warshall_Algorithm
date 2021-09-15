INF = int(1e9) # 무한대의 값으로 10억을 설정

n = int(input()) # n = 노드의 갯수
m = int(input()) # m = 간선의 갯수 입력받기
graph = [[INF] * (n+1) for _ in range(n+1)] # 2차원 리스트를 만들고 무한대의 값으로 초기화

# 자기자신에서 자기자신으로 가는 값을
for a in range(1, n+1):
    for b in range(1, n+1):
        if(a==b):
            graph[a][b] = 0 #0으로 초기화

for _ in range(m):
    a,b,c = map(int,input().split()) # 각 간선의 정보를 입력받음
    graph[a][b] = c # a에서 b로 가는 비용을 c라고 설정


# 플로이드 워셜 알고리즘

for k in range(1, n+1): # k = 거쳐가는 노드
    for a in range(1, n+1): # a = 시작노드
        for b in range(1, n+1): # b = 종료 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행결과를 출력

for a in range(1, n+1):
    for b in range(1, n+1):

        if graph[a][b] == INF: # 도달할 수 없는 경우
            print("INFINITY", end=" ")
        else: # 도달할 수 있는 경우
            print(graph[a][b], end=" ")
    print()





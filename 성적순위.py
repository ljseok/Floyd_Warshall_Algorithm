INF = int(1e9)
n,m = map(int, input().split()) # 학생들의 수, 두 학생의 성적을 비교한 횟수 입력
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b: # 자기자신에서 자기자신으로 오는 비용
            graph[a][b] = 0 # 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1 # a에서 b로 가는 비용을 1로 설정

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 학생을 번호에 따라 확인하면서 도달가능한지 체크
for a in range(1,n+1):
    cnt = 0
    for b in range(1,n+1):
        if graph[a][b] != INF or graph[b][a] != INF: # 도달할 수 있다면
            cnt += 1
    if cnt == n:
        result += 1
print(result)


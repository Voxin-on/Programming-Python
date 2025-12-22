def deikstra(r1, c1, r2, c2):

    dist = [[float('inf')] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    dist[r1][c1]=0

    for _ in range(N*M):
        min_val = float('inf')
        curr_r, curr_c = -1, -1

        for r in range(N):
            for c in range(M):
                if not visited[r][c] and dist[r][c] < min_val:
                    min_val = dist[r][c]
                    curr_r, curr_c = r, c

        if curr_r == -1: break
        if curr_r == r2 and curr_c == c2: return dist[r2][c2]

        visited[curr_r][curr_c] = True

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = curr_r + dr, curr_c + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if abs(setka[nr][nc] - setka[curr_r][curr_c]) <= 100:
                    if dist[nr][nc] > dist[curr_r][curr_c] + 1:
                        dist[nr][nc] = dist[curr_r][curr_c] + 1
    return dist[r2][c2]


def aStar(r1, c1, r2, c2):
    N = len(setka)
    M = len(setka[0])

    g = [[float('inf')] * M for _ in range(N)]
    f = [[float('inf')] * M for _ in range(N)]
    state = [[0] * M for _ in range(N)]

    g[r1][c1] = 0
    f[r1][c1] = abs(r1 - r2) + abs(c1 - c2)
    state[r1][c1] = 1
    open_list = [(r1, c1)]

    while True:
        min_f = float('inf')
        idx = -1

        for i, (r, c) in enumerate(open_list):
            if f[r][c] < min_f:
                min_f = f[r][c]
                idx = i

        if idx == -1:
            break

        curr_r, curr_c = open_list.pop(idx)

        if curr_r == r2 and curr_c == c2:
            return g[r2][c2]

        state[curr_r][curr_c] = 2

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = curr_r + dr, curr_c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if abs(setka[nr][nc] - setka[curr_r][curr_c]) <= 100:
                    new_g = g[curr_r][curr_c] + 1

                    if new_g < g[nr][nc]:
                        g[nr][nc] = new_g
                        f[nr][nc] = new_g + abs(nr - r2) + abs(nc - c2)

                        if state[nr][nc] != 1:
                            state[nr][nc] = 1
                            open_list.append((nr, nc))

    return g[r2][c2]

N,M=map(int,input().split())
setka=[list(map(int, input().split())) for _ in range(N)]
start = tuple(map(int, input().split()))
target = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))

way1=deikstra(start[0],start[1],target[0],target[1])
way2=deikstra(target[0],target[1],end[0],end[1])
way3=aStar(start[0],start[1],target[0],target[1])
way4=aStar(target[0],target[1],end[0],end[1])

print(way1+way2)
print(way3+way4)



# 2 3
# 0 1000 0
# 0 0 0
# 0 0
# 0 2
# 1 1
def dfs(now, visited, gp):
    visited[now] = 1
    for x in gp[now]:
        if visited[x] == -1:
            dfs(x, visited, gp)


def solution(n, wires):
    answer = -1
    res = 1e9

    ck_list = [1]*(len(wires)+1)
    for i in range(len(wires)):
        ck_list[i] = 0
        gp = [[] for _ in range(n+1)]
        visited = [-1]*(n+1)

        for j in range(len(wires)):
            if ck_list[j] == 0:
                continue
            u, v = wires[j]
            gp[u].append(v)
            gp[v].append(u)

        dfs(1, visited, gp)

        tmp = 0
        cnt = 0
        for k in range(1, n+1):
            if visited[k] == -1:
                cnt += 1
            else:
                tmp += 1

        tmp -= cnt

        res = min(res, abs(tmp))
        ck_list[i] = 1

    return res

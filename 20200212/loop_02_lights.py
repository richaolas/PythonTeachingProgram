N, M = map(int, input().strip().split())

lights = [True] * (N + 1)

for m in range(M):
    number = m + 1
    for idx in range(1, N + 1):
        if idx % number == 0:
            lights[idx] = not lights[idx]

#result = list(filter(lambda x:not x, lights))
result = [idx for idx in range(1, len(lights)) if not lights[idx]]
print(','.join(map(str, result)))




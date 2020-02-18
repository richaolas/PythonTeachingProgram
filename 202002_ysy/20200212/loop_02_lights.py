N, M = map(int, input().strip().split())

lights = [True] * N

for m in range(M):
    for idx in range(N):
        if (idx + 1) % (m + 1) == 0:
            lights[idx] = not lights[idx]
print(lights)
#result = list(filter(lambda x:not x, lights))
result = [idx + 1 for idx, light in enumerate(lights) if not light]
print(','.join(map(str, result)))




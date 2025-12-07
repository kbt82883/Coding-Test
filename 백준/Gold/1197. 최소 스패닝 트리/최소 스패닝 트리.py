import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]
	
def union(x,y):
	x,y = find(x), find(y)
	if x != y:
		parent[y] = x
		return True
	return False

V, E = map(int, input().split())

edges = []
for _ in range(E):
	u,v,w = map(int, input().split())
	edges.append((w, u, v))

edges.sort()

parent = list(range(V+1))
min_sum = 0
cnt = 0
for w, u, v in edges:
	if union(u,v):
		min_sum += w
		cnt += 1
		if cnt == V-1:
			break

print(min_sum)
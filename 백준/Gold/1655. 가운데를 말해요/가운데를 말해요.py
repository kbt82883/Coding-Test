import heapq
import sys

input = sys.stdin.readline

n = int(input())
maxheap = []
minheap = []

for _ in range(n):
    x = int(input())

    heapq.heappush(maxheap, -x)

    if minheap and -maxheap[0] > minheap[0]:
        a = -heapq.heappop(maxheap)
        b = heapq.heappop(minheap)
        heapq.heappush(maxheap, -b)
        heapq.heappush(minheap, a)

    if len(maxheap) > len(minheap) + 1:
        a = -heapq.heappop(maxheap)
        heapq.heappush(minheap, a)

    print(-maxheap[0])

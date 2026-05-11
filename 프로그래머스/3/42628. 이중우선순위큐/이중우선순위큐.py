import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    deleted = {}
    idx = 0

    def clean_min():
        while min_heap and deleted.get(min_heap[0][1], False):
            heapq.heappop(min_heap)

    def clean_max():
        while max_heap and deleted.get(max_heap[0][1], False):
            heapq.heappop(max_heap)

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == "I":
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            deleted[idx] = False
            idx += 1

        else:
            if num == 1:
                clean_max()
                if max_heap:
                    _, i = heapq.heappop(max_heap)
                    deleted[i] = True
            else:
                clean_min()
                if min_heap:
                    _, i = heapq.heappop(min_heap)
                    deleted[i] = True

    clean_min()
    clean_max()

    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]
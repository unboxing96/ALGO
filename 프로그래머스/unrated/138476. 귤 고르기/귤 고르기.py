from collections import defaultdict
import heapq

def solution(k, tangerine):
    counter = defaultdict(int)
    for t in tangerine:
        counter[t] += 1

    heap = [[value, key] for key, value in counter.items()]
    heapq.heapify(heap)

    remaining = len(tangerine)
    while remaining > k:
        smallest_item = heapq.heappop(heap)
        remove_count = min(remaining - k, smallest_item[0])
        smallest_item[0] -= remove_count
        remaining -= remove_count
        if smallest_item[0] > 0:
            heapq.heappush(heap, smallest_item)

    return len(heap)

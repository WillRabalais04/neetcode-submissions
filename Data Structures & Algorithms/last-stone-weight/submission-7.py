class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            print(max_heap)
            x,y = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, x-y)
        if len(max_heap) == 0:
            return 0
        print(max_heap)
        return -max_heap[0]
                
                
        
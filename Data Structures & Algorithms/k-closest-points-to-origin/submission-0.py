class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for i, (x,y) in enumerate(points):
            dists.append((math.sqrt(x**2 + y**2), i))
        heapq.heapify(dists)
        return [points[heapq.heappop(dists)[1]] for _ in range(k)]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dists = [(math.sqrt(point[0]**2+point[1]**2), point) for point in points]
        heapq.heapify(dists) # sorts by first elem in tuple
        k_closest = heapq.nsmallest(k, dists)
        ret = [dist[1] for dist in k_closest]
        print(f"dists: {dists} | ret: {ret}")
        return ret[:k]
        
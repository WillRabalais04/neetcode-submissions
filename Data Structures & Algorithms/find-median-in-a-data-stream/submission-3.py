class MedianFinder:

    def __init__(self):
        self.upper_half = list() # min heap
        self.lower_half = list() # max heap


    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower_half, -num)

        if self.upper_half and -self.lower_half[0] > self.upper_half[0]:
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)

        if len(self.lower_half) > len(self.upper_half) + 1:
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)
        elif len(self.upper_half) > len(self.lower_half):
            val = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -val)


    def findMedian(self) -> float:
        print(f"lh: {self.lower_half} uh: {self.upper_half}")
        total_length = len(self.upper_half) + len(self.lower_half)

        if total_length == 0:
            return 0.0
        if total_length == 1: 
            if len(self.lower_half) > 0:
                return -self.lower_half[0]
            if len(self.upper_half) > 0:
                return self.upper_half[0]

        if len(self.upper_half) == len(self.lower_half):
            return (self.upper_half[0] - self.lower_half[0]) / 2 
        if len(self.lower_half) < len(self.upper_half):
            return self.upper_half[0]
        else:
            return -self.lower_half[0]

        
        
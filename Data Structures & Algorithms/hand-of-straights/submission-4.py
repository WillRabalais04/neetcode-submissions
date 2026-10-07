class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = count.get(n,0) + 1
        
        mh = list(count.keys())
        heapq.heapify(mh)
        while mh:
            first = mh[0]
            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    if i != mh[0]:
                        return False
                    heapq.heappop(mh)
        return True
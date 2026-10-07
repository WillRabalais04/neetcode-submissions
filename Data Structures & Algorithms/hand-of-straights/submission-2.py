class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) < groupSize or len(hand) % groupSize != 0:
            return False

        groups = int(len(hand) / groupSize)

        hand.sort()
        
        for i in range(groups):
            idx = 0
            prev = hand.pop(0)
            popped = [prev]
            while len(popped) < groupSize and idx < len(hand):
                for j in range(groups):
                    if idx + j < len(hand) and hand[idx + j] == (prev + 1):
                        popped.append(hand[idx + j])
                        hand.pop(idx + j)
                        prev += 1
                        idx -= 1
                        break
                idx += 1
        return len(hand) == 0
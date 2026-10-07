class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) < groupSize or len(hand) % groupSize != 0:
            return False

        groups = int(len(hand) / groupSize)

        hand.sort()
        
        for i in range(groups):
            print(f"i:{i}")
            idx = 0
            prev = hand.pop(0)
            popped = [prev]
            while len(popped) < groupSize and idx < len(hand):
                print(f"idx: {idx} | prev: {prev} | hand:{hand} | popped:{popped}")
                for j in range(groups):
                    if idx + j < len(hand) and hand[idx + j] == (prev + 1):
                        popped.append(hand[idx + j])
                        print(f"POP: {hand[idx + j]}")
                        hand.pop(idx + j)
                        prev += 1
                        idx -= 1
                        break
                    else:
                        print(f"j: {j} | idx + j: {idx + j} | prev: {prev} | hand: {hand}")
                idx += 1
        print(hand)
        return len(hand) == 0
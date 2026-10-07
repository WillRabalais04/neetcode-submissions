class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = b = c = False
        for j in range(len(triplets)):
            if triplets[j][0] == target[0] and triplets[j][1] <= target[1] and triplets[j][2] <= target[2]:
                a = True
            if triplets[j][1] == target[1] and triplets[j][0] <= target[0] and triplets[j][2] <= target[2]:
                b = True
            if triplets[j][2] == target[2] and triplets[j][0] <= target[0] and triplets[j][1] <= target[1]:
                c = True
        return a and b and c
        
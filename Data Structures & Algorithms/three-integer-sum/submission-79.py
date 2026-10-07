class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSum(n, target):
            ret = []
            complement = [target - x for x in n]
            for i,x in enumerate(complement):
                ts = sorted([x,target - x, -target])
                if x in n and n.index(x) != i and ts not in ret:
                    print(str(complement) + "| x: " + str(x) + " | target: " + str(target))
                    ret.append(ts)

            return ret

        r = []

        for i in range(len(nums)):
            arr = nums[:i] + nums[i + 1:]
            c = twoSum(arr, -nums[i])
            for triplet in c:
                if triplet not in r:
                    r.append(triplet)

        return r



        
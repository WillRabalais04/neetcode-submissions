class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()        

        for i,x in enumerate(nums):
            if x > 0:
                break
            if i > 0 and x == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) -1
            while l < r:
                ts = x + nums[l] + nums[r]
                if ts < 0:
                    l +=1
                elif ts > 0:
                    r -=1
                else:
                    ret.append([x,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1
        return ret
            


        ''' O(n^3)
        def twoSum(n, target):
            ret = []
            complement = [target - x for x in n]
            for i,x in enumerate(complement):
                ts = sorted([x,target - x, -target])
                if x in n and n.index(x) != i and ts not in ret:
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

        '''
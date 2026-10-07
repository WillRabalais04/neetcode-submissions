class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def sumtwo(nums: List[int], target: int, i: int) -> List[List[int]]:
            visited = set()
            ret = []
            for num in nums:
                complement = target - num
                if complement in visited:
                    ret.append([complement, num])
                visited.add(num)
            return ret
        
        ret = []
        for i in range(len(nums)):
            arr2 = nums[:i] + nums[i+1:]
            pairs = sumtwo(arr2, -nums[i], i)
            for pair in pairs:
                triplet = sorted(pair + [nums[i]])
                ret.append(tuple(triplet))  # Convert to tuple for deduplication
        
        ret = list(set(ret))  # Remove duplicate triplets
        return [list(x) for x in ret]  # Convert back to list


        

        # def sumtwo(nums: List[int], target: int, i: int) -> List[int]:
        #     visited = set()
        #     ret = dict()
        #     for num in nums:
        #         complement = target - num
        #         if complement in visited:
        #             return [complement, num]
        #         else:
        #             print("nums: " + str(nums) + "| target: " + str(target) + "| num: " + str(num) + " | complement: " + str(complement))
        #         visited.add(num)
        #     return ret
        
        # ret = []
        # for i in range(len(nums)):
        
        #     arr2 = nums[:i] + nums[i+1:]
        #     ts = sumtwo(arr2,-1 * nums[i], i)
        #     if ts :
        #         ts.append(nums[i])
        #         ret.append(ts)

        # ret = [tuple(sorted (x)) for x in ret]
        # ret = list(set(ret))
        # return [list(x) for x in ret]




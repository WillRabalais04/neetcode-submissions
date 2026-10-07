class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # # have nums be 1 indexed
        # # [3,4,2,3,1]

        # # cases:
        # # c > (i + 1)
        #     # nums[c - 1] += 1
        #     # nums[i] = 0 // optional
        # # c = (i + 1)
        #     # nums[i] = 1
        # # c < (i + 1)
        #     # nums[c - 1] += 1
        # # indices: [1,2,3,4,5]
        # # array  : [3,1,3,4,2] | [0,1,4,4,2], [1,0,4,4,2], [1,0,0,5,2], [1,0,0,0,3], [1,0,1,0,0]
        # # output : [1,1,2,1,0]
        # for i in range(len(nums)):
        #     if nums[i] < i + 1:
        #         nums[nums[i] - 1] += 1
        #         nums[i] = 0
        #     elif nums[i] == i + 1:
        #         nums[i] = 1
        #     else:
        #         nums[nums[i] - 1] += 1
        #         nums[i] = 0


        # print(nums)

        # for i in range(len(nums)):
        #     if nums[i] > 1:
        #         return i + 1

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
            else:
                return abs(nums[i])
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return -1
                
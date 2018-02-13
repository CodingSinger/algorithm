

class Solution:
    def helper(self,nums,target):

        for index in range(len(nums)):
            if nums[index] == target:
                return index
            if nums[index] >target:
                return index
        return 0
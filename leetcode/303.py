

class Solution:
    def __init__(self,nums):
        self.nums = nums
        self.cache = [0 for x in range(len(nums))]
        for i in range(1,len(nums)):
            self.cache[i] = self.nums[i]+self.cache[i-1]



    def sumRange(self,i,j):
        return self.cache[j]- self.cache[i]+self.nums[i] #加上减去的self.nums[i]



s = Solution([1,2,3,4,5])
print s.sumRange(0,2)


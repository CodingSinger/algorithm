
class Solution:
    def helper(self,nums):

        max1 = -1
        max2 = -1
        result = -1
        for index in range( len(nums)):
           if max1 < nums[index]:
               result = index
               max2 = max1
               max1 = nums[index]
           else:
               if max2 <nums[index]:
                   max2 = nums[index]


        return result if max1>=2*max2 else -1


s = Solution()
print(s.helper([0,0,3,2]))
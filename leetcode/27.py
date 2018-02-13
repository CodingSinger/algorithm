
class Solution:
    def helper(self,nums,val):

        if not nums:
            return 0
        finish = False

        i = 0

        while not finish:
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
            if i >= len(nums):
                finish = True


        return len(nums)

s = Solution()
l = [1,2,3,5]
s.helper(l,2)
print l
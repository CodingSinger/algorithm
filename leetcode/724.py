

# 如何使得求和次数最少而得到正确答案呢
# 计算出数组所有和的结果 totalSum
# 通过遍历过程中  right‘  =  totalSum - sum(nums[0..index-1] - nums[index]     left = sum(nums[0..index-1])
# if right == left ; return index
class Solution:
    def helper(self,nums):
        totalSum = sum(nums)

        left = 0
        for index in range(len(nums)):



            if left == totalSum - left-nums[index]:
                return index

            left += nums[index]

        return -1



s = Solution()

print(s.helper([-1,-1,-1,0,1,1]))

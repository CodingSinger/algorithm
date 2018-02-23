
class Solution:


    #暴力
    def helper(self,nums):

        result = []

        for i1,n1 in enumerate(nums):
            for i2,n2 in enumerate(nums):
                for i3,n3 in enumerate(nums):
                    if i1 != i2 and i2 != i3 and i3 != i1:
                        result.append(n1*n2*n3)


        return max(result)




    #技巧法 最大的乘积 有两种可能最大的3个正数 或者最小的两个负数乘以最大的正数
    def helper2(self,nums):

        nums = sorted(nums)

        r1 = nums[0]*nums[1]*nums[-1]
        r2 = nums[-1]*nums[-2]*nums[-3]

        return max(r1,r2)




s = Solution()
print(s.helper([1,2,3,4]))
print(s.helper2([1,2,3,4]))
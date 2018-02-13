#思路 :因为是排序好的 所以只需要记录第一个不同值，并比较接下来的值，相同则移除，不同则继续保存当前值，反复如此

class Solution:
    def helper(self,nums):

        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        count = 1

        temp = nums[0]

        finish = False
        i = 1
        while not finish:

            if temp != nums[i]:
                count+=1
                temp = nums[i]
                i += 1 #只能此处才移动下标索引
            else:
                nums.pop(i) #此处索引i不动 因为pop操作之后 当前元素移除，i指向的是下一个元素 不需要i+=1



            if i >= len(nums):
                finish =True



        return count

s = Solution()
l = [1,1,2]
print s.helper(l)
print l
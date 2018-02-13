#encoding=utf-8

#因为要记录最大值 所以需要sum变量保存当前最大值 因为不能相邻则需要记录下上次取得最大值时的nums数组的下标last 不相邻则last +1 != current 除此之外需要temp变量保存sum改变之前的值，这样就能进行比较并进行回溯
class Solution:
    def helper(self,nums):


        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        sum = nums[0]
        last = 0

        temp = 0

        for current in range(1,len(nums)):




            if last +1 != current:
                temp = sum
                sum = sum+nums[current]
                last = current



            elif temp+nums[current] >sum:
                last = current
                k = sum
                sum = temp+nums[current]
                temp = k





        return sum



s = Solution()
print s.helper([2,3,2])

# 刚开始temp = 0 sum=2,到3的时候 因为相邻所以需要比较上一次结果的值加上本次的遍历值是否大于当前sum，因为0+3>2 所以决定上一家2不偷 偷3，并将temp更新为2，sum更新为3，并记下当前的current，以便后续遍历判断是否相邻

# 继续遍历2时，因为相邻所以继续比较temp+nums[current]和sum的值，因为2+2>3，所以继续更新sum=temp+nums[current]=4，并记下当前的值以及更新temp和current，dp的思想在这题的体现就是保证每一次元素遍历之后的sum是当前所能的最大的。
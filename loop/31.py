class Solution:
    def helper(self, arr):

        # res记录到目前位置最大值，sum记录加上本次遍历的值的和，如果加上之后<0了，则我们舍弃之前所有的值，从下次位置重新加
        sum, res = 0, -1

        for a in arr:
            sum = sum + a
            if sum + a < 0:
                sum = 0
            res = max(sum, res)
        return res


s = Solution()
arr = [1, -2, 3, 10, -4, 7, 2]
print(s.helper(arr))



# 牛顿法 https://zh.wikipedia.org/wiki/%E7%89%9B%E9%A1%BF%E6%B3%95

class Solution:
    def helper(self,x):
        r = x
        while r * r > x:
            r = (int)((r + x / r) / 2)
        return r * r == x

s = Solution()
print(s.helper(25))

# 数梦工场笔试
# http://blog.crayygy.com/14599905787744.html


# f(n)=f(n-1)+f(n-2) 第n级台阶的走法是在第n-1级走法上再走一步与在第n-2级走法上再走两步
class Solution:
    def helper(self, n):
        res = [0 for i in range(n)]

        res[0] = 1
        if n >= 2:
            res[1] = 2

        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res


s = Solution()
print(s.helper(10))

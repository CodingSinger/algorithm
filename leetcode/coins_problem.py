class A:
    def say(self):



# 硬币问题

class Solution:
    def helper(self,value):

        mins = [10000 for x in range(value+1)]
        coins = [1,2,3,5]
        mins[0] = 0

        for money in range(1,value+1):
            for coin in coins:
                if money-coin>=0:
                    mins[money] = min(mins[money],mins[money-coin]+1) #状态方程


        return mins[value]


s = Solution()
print s.helper(13)
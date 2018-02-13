

# 其实就是求最小值和最大值的差 但是最大值一定要在最小值的后面才行
class Solution:
    def helper(self,prices):



        if len(prices) <2:
            return 0

        profit = 0
        buy = prices[0]


        for index in range(1,len(prices)):
            if prices[index] - buy >0: #说明后面的大于前面的 故记下此时的最大利润 买进日期不必更新
                profit = max(profit,prices[index]-buy)


            else: #说明buy > prices[index] 买进日期需要更新了 因为发现了更低价格的买进日期
                buy = prices[index]

        return profit

s = Solution()
print s.helper([7,1,5,3,6,4])

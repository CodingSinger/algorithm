class Solution:
    # 时间复杂度 O(n)
    def helper(self, prices):

        prices.append(0)

        profit = 0
        flag = True  # True表示还没持有股票 False表示当前持有股票

        for i, price in enumerate(prices[:-1]):
            if prices[i + 1] > prices[i]:  # 如果明天的股价比今天的高
                if flag:  # 但是还没有持有股票,则今天买
                    inday = i
                    flag = False
                else:  # 已经持有股票了则今天先不卖
                    pass


            else:  # 明天股价下跌了
                if not flag:  # 当前买入过股票，赶紧在最高点卖出  就算之后有更高点 也是现在卖之后再买进来卖合算
                    # 比如[5,4,8,20,19,40,7,3]，4的时候买进，20卖出，再从19买入，40卖出一定比4买入，40卖出合适，分别设这4个点为a<b>c<d 则（b-a)+(d-c)>=(d-a)一定成立
                    flag = True
                    profit = profit + price - prices[inday]

        return profit


    #这种方法更为巧妙，贪婪地把每一天上涨的都直接进行相加
    def helper2(self, prices):

        profit = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i - 1]:#如果今天多于昨天，则默认为昨天买今天卖
                profit += prices[i] - prices[i - 1]

        return profit

    #one liner
    def helper3(self,prices):
        return sum([prices[i]-prices[i-1] if prices[i]>prices[i-1] else 0 for i in range(1,len(prices))])



s = Solution()
print(s.helper([5, 4, 8, 20, 19, 40, 7, 3]))
print(s.helper2([5, 4, 8, 20, 19, 40, 7, 3]))
print(s.helper3([5, 4, 8, 20, 19, 40, 7, 3]))
print(s.helper([1, 2]))

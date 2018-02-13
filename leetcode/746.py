
#encoding=utf-8
class Solution:
    def helper(self,cost):



        if len(cost) <=1:
            return 0
        r = cost[0]


        min1,min2 = cost[0],cost[1]


        # 状态转移方程 r = min(min1,min2)+cost[i]
        # min2 为取每次跳一步或者两步的最小值
        # min1 保存上次没跳的值 以便于后一次循环跳两步比较


        for index in range(2,len(cost)):

            min1,min2= min2,min(min1,min2)+cost[index]

        return min(min1,min2)


s = Solution()
print(s.helper([1,2,100,200,1,4]))

# 第一次循环后min1 = 1,min2 = 3 ，保存min2的值是为了之后，再一次循环 min1 = min2 = 3,min2 = 103，继续循环.令min1 =min2 ，即保存
# 上一步时的总步数，以便在下一次循环中min1+cost[index] 表示的是上上步跳两步的总步数 因为min2 = min(min1,min2)+cost[index] 所以min2
# 始终表示走过当前index的总步数， 每一次循环未改变时min1表示上上一步时的总步数，min2表示上一步时的总步数，然后min(min1+min2)来判断走一步或者是两步到当前地方哪个比较省





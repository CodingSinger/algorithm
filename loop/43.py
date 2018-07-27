
# 统计每个点数出现的次数，我们可以参照28题的思路，一个一个来计算。28题是计算每个位置的可能性
class Solution:
    def helper(self, n):

        cur = [[0 for i in range(6 * n + 2)] for row in range(n + 2)]
        pre = [[0 for i in range(6 * n + 2)] for row in range(n + 2)]
        cur[1] = [1 if 6 >= i >= 1 else 0 for i in range(6 * n + 2)]

        for i in range(2, n + 1):
            cur, pre = pre, cur
            # cur.append([0 for n in range(i * 6 + 2)])
            for j in range(i, 6 * i + 1):
                #加上这颗骰子之后，因为这颗骰子可能摇1-6之间某个数，所以摇到j这个点数的次数为不要这颗筛子之前摇到j-1,j-2,j-3,j-4,j-5,j-6的次数的总和
                for k in range(1, 7):
                    if j - k >= 0:
                        cur[i][j] += pre[i - 1][j - k]

        return cur if n % 2 == 0 else pre


s = Solution()
print(s.helper(5))

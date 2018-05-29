
# 状态：LCS[i+1,j+1]，表示字符串X的X[0..i]和字符串Y的Y[0..j]之间最长公共子序列长度

# 状态转移方程： LCS[i+1,j+1] = LCS[i,j]+1 if X[i] == Y[j] else max(LCS[i+1,j],LCS[i,j+1])


class Solution:
    def helper(self, x, y):
        lx, ly = len(x), len(y)
                    # """列"""                             """行"""
        lcs = [[0 for i in range(ly + 1)] for j in range(lx + 1)]

        for i in range(lx):
            for j in range(ly):
                if x[i] == y[j]:
                    lcs[i + 1][j + 1] = lcs[i][j] + 1
                else:
                    lcs[i + 1][j + 1] = max(lcs[i + 1][j], lcs[i][j + 1])

        return lcs[lx][ly]


s = Solution()
print(s.helper("ABCDCF", "BBGCD"))

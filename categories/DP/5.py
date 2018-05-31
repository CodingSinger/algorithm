class Solution:
    def helper(self, s):
        ls = len(s)
        x = [1 for i in range(ls)]

        maxi = 0
        for k in range(ls):
            for i in range(0, ls):
                for j in range(i, ls):
                    temp = s[j + 1:k + 1]
                    if s[i:j + 1] == temp[::-1]:
                        x[k] = max(k - i + 1, maxi)
                        maxi = x[k]
            x[k] = max(maxi, x[k])
        return x[ls - 1]

    def helper1(self, s):
        ls = len(s)
        x = [[0 for i in range(ls+1)] for j in range(ls+1)]
        rs = s[::-1]

        # 查找公共子串

        ans, start, end, res = 1, 0, 0, ""
        for i in range(ls):
            for j in range(ls):
                if s[i] == rs[j]:
                    x[i+1][j+1] = x[i][j] + 1
                    if ans <= x[i+1][j+1]:
                        # 检查是不是回文
                        temp = s[i - x[i+1][j+1] + 1:i + 1]
                        if temp == temp[::-1]:
                            res = temp
                            ans = x[i+1][j+1]

        return res


s = Solution()
print(s.helper1("abb"))

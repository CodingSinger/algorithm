class Solution:

    # 步骤：
    # 状态定义：f[i] 表示s[0:i]之间的都能在dict中找到单词
    # 状态转移方程： if f[i] == True and s[i:k] in dict: f[k] = True //如果f[i]为真并且s[i:k]的单词也能在字典找到，则f[k] = True
    def helper(self, s, wordDict):

        f = [False] * (len(s) + 1)
        f[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break

        return f[len(s)]




str = "applepenapple"
wordDict = ["apple", "pen"]
s = Solution()
print(s.helper(str, wordDict))

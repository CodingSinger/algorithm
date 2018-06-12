class Solution:


    # 基于139题的思路 但是超时了...
    def helper(self, s, wordDict):

        f = [False] * (len(s) + 1)
        f[0] = True
        ans = {}
        for i in range(len(s) + 1):
            for j in range(0, i):
                if f[j] and s[j:i] in wordDict:
                    if j not in ans:
                        ans[i] = [s[j:i]]
                    else:
                        length, cur = len(ans[j]), 0
                        if i not in ans:
                            ans[i] = []
                        # 把之前已经分布在字典里的子串取出来然后加上本次在字典里的字符串
                        while cur < length:
                            temp = ans[j][cur]
                            ans[i].append(temp + " " + s[j:i])
                            cur += 1
                    f[i] = True
        # return f[len(s)]
        return [] if len(s) not in ans else ans[len(s)]


s = Solution()
st = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(s.helper(st, wordDict))

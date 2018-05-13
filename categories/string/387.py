import collections


class Solution:
    # 本地运行正确但是 leetcode错误
    def helper(self, s):

        c = collections.Counter(s)

        for k, v in c.items():
            if v == 1:
                return s.index(k)
        return -1

    def helper2(self, s):
        for i, c in enumerate(s):
            # 往前往后都没有
            if c not in s[i + 1:] and c not in s[:i]:
                return i
        return -1

    def helper3(self, s):

        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c]+1

        for k, v in d.items():
            if v == 1:
                return s.index(k)
        return -1


    def helper4(self,s):
        letters='abcdefghijklmnopqrstuvwxyz'
        # 将count为1的字符下标都存起来 取索引最小的
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


s = Solution()
print(s.helper2("leetcode"))
print(s.helper3("leetcode"))

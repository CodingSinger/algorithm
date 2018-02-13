# 思路：第一个为临时结果，比较接下里的所有字符串，每次比完以该次比较结果前缀为临时结果继续和下一个字符串比较
class Solution:
    def helper(self,strs):
        if len(strs) == 0:
            return ""
        temp = strs[0]
        result = ""
        for s in strs:
           length = len(s) if len(s)<len(temp) else len(temp)
           for i in range(length):
               if temp[i] == s[i]:
                   result += s[i]
               else:
                   break

           temp = result
           result = ""
        return temp





s = Solution()
print s.helper(['aa','ab'])


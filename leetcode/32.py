
# 该题的思路
class Solution:
    def helper(self, s):
        stack = []
        s += '(' #再加一个字符以触发遍历到最后的max比较
        res = 0
        for index in range(0, len(s)):
            c = s[index]
            if not stack:
                res = max(res, index)
                stack.append(index)
                continue
            top = stack[-1]
            if c == '(':
                stack.append(index)
                res = max(res, index - top - 1)
            else:
                temp = s[top]
                if temp == '(':
                    stack.pop()
                else:
                    stack.append(index)
                    res = max(res, index - top - 1)

        return res


s = Solution()
print(s.helper("()"))
print(s.helper("(()())(()"))


#思路：用栈的思想 遇到左括号则把对应的右括号放入栈中，遇到右括号则判断是否和栈顶元素一致 不一致则不符合最后一次左括号的匹配要求 一致则栈顶元素出栈
class Solution:
    def helper(self,s):


        map = {"[":"]","{":"}","(":")"}
        temp = []

        length = len(s)

        for i in range(length):
            if map.has_key(s[i]):
                temp.append(map[s[i]])
            else:
                if len(temp) == 0:
                    return False
                if temp[len(temp)-1] != s[i]:
                    return False
                else:
                    temp.pop()


        if len(temp) != 0:
            return False
        return True










s = Solution()
print s.helper("(({])）")
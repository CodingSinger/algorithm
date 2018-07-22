

# 反转字符串 hello world = world hello
class Solution:
    def helper(self,str):
        ss = str.split(" ")
        ss = ss[::-1]
        print(ss)


    def helper2(self,str):
        str+=" " #最后再加个“ ”保证最后一个单词也被加入集合
        temp = ""
        a = []
        for s in str:
            if s == ' ':
                a.append(temp)
                temp = ""
                continue
            temp +=s
        print(a[::-1])

s = Solution()
print(s.helper("hello im your baby"))
print(s.helper2("hello im your baby"))
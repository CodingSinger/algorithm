
# 关于涉及检验字符串中某个字符在或不在的题目，都可以用数组保存256个字符作为下标，
# 模拟哈希表的形式，python ord(x) 表示获取某字符的对应数字，chr(x)表示对应某数字的字符


# A字符串删去B字符串中出现的字符，
class Solution:
    def helper(self,A,B):

        dit = [0]*256
        for c in B:
            dit[ord(c)] = 1
        cur = ""
        for c in A:
            if dit[ord(c)] == 0:
                cur +=c

        return cur


# 删除字符串中重复出现的字符 google -> gole
class Solution2:

    def helper(self,S):
        dit = [0] * 256
        cur = ""
        for c in S:
            if dit[ord(c)] != 1:
                cur +=c
                dit[ord(c)] = 1
        return cur




s = Solution()
print(s.helper("We are students","aeiou"))

print(Solution2().helper("google"))



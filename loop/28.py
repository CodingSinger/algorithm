

# 思路就是将大字符串转换成小字符串，然后拼接起来，得到所有可能。
# 即对任意一个字符串来说，都获得第一个位置的所有可能，设为a1，然后将剩下的字符串，再次去获得第一个位置的所有可能，为a2,递归下去，当剩下的字符串为“”时，则说明说有位置都取完可能性，每一次结束时得到的拼接a1a2..an即为
# 所有可能性中的一种
# 距离来说 abc 首先遍历abc，得到第一个位置的所有可能 a ,b ,c ,分别将剩下的字符串bc,ac,ab再次进行遍历，
# 对这三种情况得到第一个字符的可能
# a: b-c ,c-b ,对该情况再次对剩下的子串c,b获取第一个元素的可能，当然只有一个字符了，所以该情况下的可能性为abc,acb，下面的两种情况也是一样分析
# b: a-c, c-a
# c: a-b, b-a
# 通过该方法再长的字符串也能转化为小字符串慢慢解决
# 与该题类似的有爬楼梯问题，无论楼梯有多长，从第一阶楼梯开始计算起，后面的都依赖之前的计算，从而得到最终结果

class Solution:



    def helper(self,str):

        all = []
        def permutation(pre,s):
            if not s:
                all.append(pre)
            for i in range(len(s)):
                permutation(pre+s[i],s[:i]+s[i+1:])

        permutation("",str)

        return all



s = Solution()
print(s.helper("abcd"))
print(set(s.helper("abcd")))
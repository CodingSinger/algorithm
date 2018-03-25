
class Solution:
    # def helper(self,n):
    #     if n<=26:
    #         return chr(n+64)
    #     return self.res(n)
    #
    # def res(self,nums):
    #     remainer = nums % 26
    #     nums = nums // 26
    #
    #     if nums == 0:
    #          return chr(remainer+64)
    #
    #
    #     return self.res(nums)+chr(remainer+64)

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        return self.res(n)

    def res(self, nums):
        remainer = (nums - 1) % 26 #理解为什么需要减一
        nums = (nums - 1) // 26

        if nums == 0:
            return chr(remainer + 65)

        return self.res(nums) + chr(remainer + 65)

# n = len(result)

# nums -> 26^(n-1)x ord(s[n-1])-64+...+26^0xord(s[0]

#例如 result = "BAC" n = 3  nums = 26^2*2+26^1*1+26^0*3

#  We can’t simply use the n%26 method because:
#
# ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26
#
# We can use (n-1)%26 instead, then we get a number range from 0 to 25.

print(ord("C"))
s = Solution()
print(s.convertToTitle(26*26*2+26*1+26*0+3))


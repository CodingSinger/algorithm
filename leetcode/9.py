
#回文整型数字

#思路：将传入参数x反转 比较是否相等
class Solution:
    def isPalindorome(self,x):

        temp = x
        y = 0
        while x>0:
            y = y*10+x%10
            x = x/10

        return temp == y


s = Solution()
print  s.isPalindorome(9)
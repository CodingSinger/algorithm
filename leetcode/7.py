
#思路：反转int

class Solution:
    def reverse(self,x):

        if x>2**31:
            return 0
        temp = 0
        if x<0:
            temp = x
            x = -x


        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x / 10


        if y>2**31:
            return 0
        if temp<0:
            return -y
        return y


s = Solution()
print  s.reverse(1534236469)

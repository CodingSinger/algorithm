
class Solution:
    def helper(self,digits):

        add = 1
        length = len(digits)
        for i in range(length-1,-1,-1):
            digits[i] = digits[i] + add
            add = digits[i] / 10
            if digits[i] >=10:

                digits[i] = digits[i] %10

                if i == 0:
                    digits.insert(0,1)
        return digits


s = Solution()
print s.helper([9,9,9,9,9])






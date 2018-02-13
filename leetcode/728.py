
class Solution:
    def helper(self,left,right):

        by = 10
        result = []


        for i in range(left,right+1):

            flag = True
            for c in str(i):
                if c == '0' or i % int(c) != 0:
                    flag = False
                    break

            if flag:
                result.append(i)




        return result




s = Solution()

print(s.helper(1,101))
import math


class Solution:
    def helper(self,c):
        final = c //2+1

        for i in range(final):

            p1 = pow(i,2)
            final2 = c -p1 // 2 +1
            for j in range(final2):
                if pow(j,2)+p1 == c:
                    return True



        return False

    #mem time exceeded  java实现的该方法能通过
    def helper2(self,c):
        final = int(math.sqrt(c))+1

        for i in range(final):
            p1 = pow(i,2)
            # search in 0..(c-final)//2+1
            end = int(math.sqrt(c-p1))+1
            start = 0
            seach = c-p1
            while start<=end:
                mid = (end-start)//2+start
                mid_2 = pow(mid,2)
                if mid_2<seach:
                    start=mid+1
                elif mid_2>seach:
                    end = mid-1
                else:
                    return True

        return False

    def helper3(self,c):

        end = int(math.sqrt(c))+1
        for i in range(end):
            b = c-pow(i)
            r = int(math.sqrt(b))
            if r * r == b:
                return True
        return False

s = Solution()
print(s.helper2(2147483641))
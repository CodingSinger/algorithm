
class Solution:
    def helper(self,x,maxWeight):
        x.sort()


        i,k = 0,len(x)-1
        if 2 * x[0]  > maxWeight:
            return k+1

        result = 0
        while i < k:
            if x[i]+x[k] <= maxWeight:
                result+=1
                i+=1
            k -= 1


        result = len(x)-2*result+result

        return result

s = Solution()

x = [2,3,5,6,8]
print(s.helper(x,8))


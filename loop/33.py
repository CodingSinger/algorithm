
from functools import cmp_to_key

class Solution:
    def helper(self,arr):

        def cmp(x,y):
            m = str(x)+str(y)
            n = str(y)+str(x)
            if m < n:
                return -1
            if m == n:
                return 0
            else:
                return 1

        return sorted(arr,key=cmp_to_key(cmp))


s = Solution()
arr = [3,32,321]
print(s.helper(arr))
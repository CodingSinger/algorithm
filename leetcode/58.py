

class Solution:
    def helper(self,s):
        l = s.split()



        return len(l.pop()) if l else  -1


s = Solution()
print s.helper("Hello world")

print s.helper(" ")
print " ".split()


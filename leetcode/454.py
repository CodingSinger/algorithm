
#典型的以空间换时间的算法 若以4层循环来做 内层用二分法来做 其时间复杂度为O(n^3logn)
class Solution:
    def helper(self,A,B,C,D):
        hashtable = {}
        for a in A:
            for b in B:
                if a + b in hashtable:
                    hashtable[a + b] += 1
                else:
                    hashtable[a + b] = 1
        count = 0
        for c in C:
            for d in D:
                if -c - d in hashtable:
                    count += hashtable[-c - d]
        return count

s = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(s.helper(A,B,C,D))
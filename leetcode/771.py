

class Solution:
    def helper(self,J,S):

        count = 0
        for s in S:
            for j in J:
                if s == j:
                    count+=1


        return count

    def helper2(self, J, S):



        cache = [0 for x in range(len(S))]
        count = 0
        for index in range(len(S)):
            if cache[index] == 1:
                count+=1
                continue
            for j in J:
                if S[index] == j:
                    count += 1
                    cache[index] = 1

        return count

    def helper3(self,J,S):
        return sum(map(S.count, J))  # this one after seeing https://discuss.leetcode.com/post/244105


s = Solution()
print(s.helper("aA","aAAbb"))
print(s.helper2("aA","aAAbb"))
print(s.helper3("aA","aAAbb"))

print(sum(map("aAAbb".count,"aA")))
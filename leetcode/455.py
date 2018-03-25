class Solution:

    #时间复杂度 O(n^2)
    def helper(self,g,s):
        count = 0
        g.sort()
        s.sort()

        for i in g:
            l = 0
            while l<len(s):
                if s[l] >= i:
                    count+=1
                    s.pop(l)
                    break

            if l == len(s): #如果最后一个都满足不了这个child了，那之后需求更大的child更加满足不了，所以直接返回
                return count

        return count



    def helper2(self,g,s):
        g.sort()
        s.sort()

        childi = 0
        cookiei = 0

        while cookiei < len(s) and childi < len(g): #使用一层循环，O(nlogn)
            if s[cookiei] >= g[childi]:
                childi += 1
            cookiei += 1


        return childi


s = Solution()
print(s.helper([1,2],[1,2,3]))
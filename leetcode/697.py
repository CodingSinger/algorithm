class Solution:
    def helper(self,nums):


        nodup = set(nums)


        left = {}
        right = {}
        count = {}



        for index,e in enumerate(nums):
            if e in count:
                count[e]+=1
                right[e] = index
            else:
                #不在
                count[e] = 1
                left[e] = index
                right[e] = index

        maxl = max(count.values())

        r = len(nums)
        for e in nodup:
            if count[e] == maxl:
                r = min(r,right[e]-left[e]+1)

        return r













s = Solution()
# print(s.helper([1,2,2,3,1]))
print(s.helper([1]))
# print(s.helper([1,2,2,3,1,4,2]))




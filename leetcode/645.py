class Solution:
    def helper(self,nums):

        map = {}

        result = []
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] = 2
        for i in range(len(nums)):
            if i+1 not in map:
                result.insert(1, i + 1)
                continue
            if map[i+1] == 2:
                result.insert(0,i+1)


        return result

s = Solution()
print(s.helper([3,2,3,4,6,5]))



from collections import Counter

class Solution:
    def helper(self,nums,k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)



nums = [4, 3, 2, 3, 5, 2, 1]
nums = [2,2,10,5,2,7,2,2,13]
s = Solution()
print(s.helper(nums,3))


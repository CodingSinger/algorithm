from collections import Counter

class Solution:
    def helper(self,nums,k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                #如果当前组能加上 v，则加上该v，然后往后递归
                if group + v <= target:
                    groups[i] += v
                    # 如果后续的search()返回false，则必须回溯到之前的状态 即groups[i]-=v 并且将之前pop的都重新append进去
                    if search(groups):
                        return True

                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False

        nums.sort()
        # 如果最大元素大于target,则可能无法划分
        if nums[-1] > target: return False
        # 将nums等于target的都去掉
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)



# nums = [1,1,1, 1]
nums = [2,2,2,2,3,4,5]
s = Solution()
print(s.helper(nums,4))


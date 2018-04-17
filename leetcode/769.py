class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:



    #自己的方法：比较难懂，思路其实挺简单的，就是不知道为啥实现起来这么麻烦： 比如一个数组 [1, 0, 2, 8, 5, 10, 6, 7]，题目说数组是0..length-1排列，但是我实现成了无论数据是如何分布的
    # 先取出最小值，0，然后划分为[1,0]和[2,8,5,10,6,7] 记为A,B,找出A中最大值和B中最小，如果不存在则说明，[1,0]肯定是有序的，可以先入队
    # 将剩下的数组[2,8,5,10,6,7]继续这样处理，[2]入队
    # [8,5,10,6,7]还是这样处理，划分为[8,5],[10,6,7],此时A中最大为8，B中最小为6,则划分为[8,5,10,6],[7]，此时A中最大，还是大于B中最小，于是将B中元素7也划分进去。
    def helper2(self, arr):
        start, past, length = 0, 0, len(arr)
        temp = arr  # temp表示为分的数组
        res = []
        while start < length:
            flag = False
            mini = min(temp)
            i = arr.index(mini)

            maxi = max(arr[start:i + 1])
            if i + 1 == length:
                mini = maxi
            else:

                mini = min(arr[i + 1:])

            while mini < maxi and i < length - 1:
                maxi = max(arr[past:i + 1])
                mini = min(arr[i + 1:])
                last = i  # 保存上次
                i = arr.index(mini)

                flag = True

            if mini > maxi and flag:
                res.append(arr[start:last + 1])
                start = last + 1
            else:
                res.append(arr[start:i + 1])
                start = i + 1

            past = start
            temp = arr[start:]

        return res


    #思路：该方法是标准答案，按照了题目的意思即数组元素分布在0..length-1之间


    # k元素一定会在下标为k+1之前找到比他更大的。如果找到了k个比他小的，则说明后面都是比k大的，则k之前的元素都可以有序
    # 例如 2,3,0,1,5,4,6,7
    # 最大的为3时，应该在下标为3的地方，已经找到了3个比3小的，则说明2，3，0，1一定是可以重新组合有序的。

    #该方法比较精妙。但是只能用于某些特定情形。
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i:
                ans += 1
        return ans


"""测试"""
arr = [1, 0, 2, 3, 2.5, 4, 2.8, 2.9]

arr1 = [1, 2, 0, 3, 5]
arr2 = [2, 0, 1, 3]

arr3 = [1, 0, 2, 3, 4]
arr4 = [2, 0, 1, 7, 3, 4, 5, 6]
arr5 = [-2,-3,-1,-0.5]
s = Solution()


print(s.helper2(arr))
print(s.maxChunksToSorted(arr))

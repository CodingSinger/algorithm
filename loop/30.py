import math


class Solution:

    # 该解法思路和29一样，29是求中位数mid的下标，这题是用快排+二分求k的下标，因为我们知道，一次快排分区之后，求出位于x处的元素，并且[0,x)都是比arr[x]小的，(x,len(arr-1]都是比arr[x]大的，所以
    # 我们只要求出第x小的数，则[0.x)之间就是最小的k个数
    # 这种解法有个问题，因为分区的时候需要移动元素，所以对于分布在多个机器上的数据不好使用，因为移动不方便 但是对于海量数据的情况下，可以使用分治mr的思想，拆成多堆数据，多个机器同时处理求出各自的前k个最小数。
    # 最后合并到一起求前k个数
    def helper(self, arr, k):
        def sort(start, end):
            guard = arr[start]
            temp = start

            while start < end:
                while start < end and arr[end] >= guard:
                    end -= 1
                while start < end and arr[start] <= guard:
                    start += 1
                if start < end:
                    arr[start], arr[end] = arr[end], arr[start]

            arr[temp], arr[start] = arr[start], arr[temp]

            return start

        start, end = 0, len(arr) - 1
        while start <= end:  # 需要start = end的情况
            index = sort(start, end)
            if k == index:
                return arr[0:k]
            elif k > index:
                start = index + 1
            else:
                end = index - 1

        return []

    # 构建k个元素的大顶堆 叶子节点x = 非叶子节点y+1    2y+1 = len(arr),可得最后一个叶子节点的下标为math.ceil((len(arr)-1)//2)
    # 对于非叶子x,两个叶子2x+1和2x+2
    def helper2(self, arr, k):

        noLeaf = math.ceil((k - 1) // 2)

        def buildHeap():
            # 从下往上置换
            for i in range(noLeaf, -1, -1):
                if 2 * i + 2 >= k:
                    # 说明没右子树
                    right = float("-inf")
                else:
                    right = arr[2 * i + 2]
                if arr[2 * i + 1] > right:
                    arr[i],arr[2*i+1] = arr[2 * i + 1],arr[i]
                else:
                    arr[i] = right

        buildHeap() #构建大顶堆
        for i in arr[k:]:
            if i < arr[0]:  # 小于堆顶
                arr[0] = i
                buildHeap() #置换之后需要重新构建大顶堆 使最大元素始终在最上面

        return arr[0:k]


s = Solution()
print(s.helper([4, 5, 4, 23, 2, 23, 31, 4], 4))
print(s.helper2([4, 5, 4, 23, 2, 23, 31, 4], 4))

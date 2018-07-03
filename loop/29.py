# 求数组中超过一半的数

# 思路：如果存在超过一半的数，则该数一定在排序之后的中位数,则我们只要判断中位数是否占有数组一半以上即可
# 那么核心问题就转化成如何最快得到中位数，全部排序取中间？如果数据量过大的话，这种方法是不可行的
# 该问题类似于求乱序大数组中的第k个元素，结合快排的元素定位+二分法 能够最大效率地找到某个位置的数,获取当我们可以移动数组的情况下(大数据情况下分机不能使用该思路)求最大或者最小的k个数 (无序)
# 例如，要求第k个元素，先求出某个元素在有序数组的下标x,因此此时数组0-x之间都小于x的乱序元素，x-len(arr)是大于x的乱序元素集合，若该x小于k,则我们要求出的
# 第k个元素一定在0-x之间，否则在x-len(arr)之间，我们利用二分法不断缩小这个范围，最终找到第k个元素。


class Solution:
    def helper(self, arr):
        def quickSort(start, end):
            guard = arr[start]
            temp = start
            while start < end:

                while start < end and arr[end] >= guard:
                    end -= 1
                while start < end and arr[start] <= guard:
                    start += 1

                if start < end:
                    arr[end], arr[start] = arr[start], arr[end]

            arr[start], arr[temp] = arr[temp], arr[start]
            return start

        def handle(arr):

            mid = len(arr) >> 1
            start, end = 0, len(arr) - 1
            index = quickSort(0, end)
            while index != mid:
                if index < mid:
                    start = index + 1
                if index > mid:
                    end = index - 1

                index = quickSort(start, end)

            num = arr[index]

            return num if arr.count(num) > len(arr) >> 1 else -1

        return handle(arr)

    # 思路二：利用数组的特点 巧妙

    # 一个数超过一半，则说明该数出现的次数一定大于其他所有的数，则我们遍历，如果当前数和上一个数一样则次数加1，不一样则减1，如果次数为0，则将当前数保存下来，并且次数置一，
    # 则遍历到最后如果计数大于等于1，则说明有一个数大于其他所有数的之和。则返回该数。2，3，2，3，3，3，5

    def helper2(self, arr):
        count, temp = 0, -1
        for i in arr:
            if count == 0:
                temp = i
                count = 1
            elif temp != i:
                count -= 1
            else:
                count += 1

        return temp if count >= 1 else -1


s = Solution()
print(s.helper([2, 3, 5, 2, 2, 2, 3, 3, 3, 3, 3]))
print(s.helper2([2, 3]))

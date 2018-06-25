# 无序数组，使其 奇数在前 偶数在后
import copy


class Solution:
    # O(n^2) 最容易想到的方法，从前遍历，偶数则放到最后，移动之前的元素。
    def helper(self, x):

        pass

    # 构造一个空数组，遍历，将偶数奇数依次放置，时间复杂度 O(n),空间复杂度O(n)
    def helper2(self, x):
        c = copy.copy(x)

        prev, back = 0, len(x) - 1
        for i in x:
            if i % 2 == 0:
                c[back] = i
                back -= 1
            else:
                c[prev] = i
                prev += 1
        return c

    # 双指针 在原数组的基础上 进行交换 时间复杂度O(n) 空间复杂度O(1)
    def helper3(self, x):
        prev, back = 0, len(x)-1

        while prev < back:
            while prev <back and x[prev] % 2 != 0:
                prev += 1
            while prev < back and x[back] % 2 == 0:
                back -= 1

            x[prev],x[back] = x[back],x[prev]

        return x


s = Solution()
x = [3,23,54,2,3,45,65]
print(s.helper2(x))
print(s.helper3(x))

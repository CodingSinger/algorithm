class Solution:
    # 思路很简单：遍历nums2将小的nums[k]插入到nums[i]前面
    def helper(self, nums1, m, nums2, n):

        i, k = 0, 0
        finish = False
        while not finish:

            if i >= k + m or k >= n:  # 注意i>=k+m 而不是i>=m ,因为随着插入数组长度会变大，k表示已经插入的长度
                break

            if nums1[i] > nums2[k]:
                nums1.insert(i, nums2[k])

                k += 1  # nums2已经插入一个 后移一个

            i += 1  # 不管有没有插入 都要后移，如果插入了则在nums1的i之前多了一个元素，数组后移导致当前数的索引升高1
            # 没有插入则说明当前nums1[i]<nums2[k]，需要往更大的数寻找 所以i+=1

        if i >= m:
            nums1[0:m + n] = nums1[:m + k] + nums2[k:]

        cut = len(nums1) - m - n

        for i in range(cut):
            nums1.pop()


    #因为题目要求在nums1数组上改动，因为从前到后进行比较则只能插入，这样的话，会使数组移动。而题目说nums1有足够的空间，则从后面往前进行比较，则不会引起数组的移动，自然效率也越高
    #如果题目不要求在原数组进行改动，则我们用第三个数组的话会更加省力，只需要比较大小放入第三个数组即可。

    def helper2(self, nums1, m, nums2, n):



        pos = m + n - 1
        m, n = m - 1, n - 1

        while m >= 0 and n >= 0:

            if nums1[m] > nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
            else:
                nums1[pos] = nums2[n]
                n -= 1
            pos -= 1
        nums1[m + 1:pos + 1] = nums2[m + 1:pos + 1]

    #因为插入的话会使原数组的索引发生变化 对于比较不方便 所以不妨创建个拷贝数组用来比较，原数组用来当做空数组插入
    def helper3(self,nums1,m,nums2,n):

        copya = nums1.copy()

        i,k = 0,0
        while i < m and k<n:
            if copya[i] > nums2[k]:
                nums1[i+k] = nums2[k]
                k+=1
            else:
                nums1[i+k] = copya[i]
                i+=1

        nums1[i+k:] = copya[i:m] if i < m else nums2[k:]


s = Solution()
l1 = [4, 0, 0, 0, 0, 0]
l2 = [1, 2, 3, 5, 6]
s.helper3(l1, 1, l2, 5)
print(l1)
l3 = [1]
l4 = []
s.helper2(l3, 1, l4, 0)
print(l3)

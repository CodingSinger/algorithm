class Solution:

    # 滑动窗口  例如 a b c d c s 当遍历到c时，发现与之前的子串(abcd)有元素c重复，我们需要把当前元素在之前子串位置之前的元素包括自己都移除。新子串为(dc)，如何进行滑动这个距离。就是解题关键
    def helper(self, s):
        dic = set()  #dic始终保存上个不重复子串的元素
        ls = len(s)
        ans = float("-inf")
        start, current = 0, 0
        while start < ls and current < ls:

            # 如果不在dic中，则不重复，添加进dic,并更新current
            if s[current] not in dic:
                dic.add(s[current])
                ans = max(ans, len(dic))
                current += 1
            else:
                # 一边删除之前的元素，一边移动，直到s[current]与dic中没有重复，即删除完毕。
                dic.remove(s[start])
                start += 1
        return ans
    # 优化 用hashMap直接记录重复元素的位置，直接进行移动即可，而不需要上面代码后续的移动来找到滑动。

s = Solution()
print(s.helper("abcbs"))

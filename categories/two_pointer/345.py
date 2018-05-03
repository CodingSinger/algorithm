class Solution:


    # 双指针思路：两个索引分从头和从尾搜寻元音，都搜索到了则进行交换，没有搜索到则根据情况索引进行加减
    def helper(self, s):
        vowels = "aeiouAEIOU"
        s = list(s)
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] in vowels and s[end] in vowels:
                # 交换
                s[start], s[end] = s[end], s[start]
                start, end = start + 1, end - 1
            else:
                if s[start] in vowels:
                    end -= 1
                elif s[end] in vowels:
                    start += 1
                else:
                    start, end = start + 1, end - 1

        return "".join(s)

s = Solution()
print(s.helper("a."))
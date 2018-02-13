
#coding=utf-8
class Solution:


    # 暴力解法
    def helper(self,haystack,needle):

        if haystack == needle or needle =="":
            return 0
        length = len(haystack)
        for index in range(length-len(needle)+1): #超过部分不需要遍历 因为长度比needle小肯定不相等

            # j = 0
            # i = index
            # while j<len(needle) and i<length:
            #
            #     if haystack[i] == needle[j]:
            #         i += 1
            #         j += 1
            #     else:
            #          break
            # if j == len(needle):
            #     return index

            if haystack[index:len(needle)+index] == needle:
                return index



        return -1






    # https://www.cnblogs.com/zhangtianq/p/5839909.html
    # KMP解法
    def findMaxLength(self,str):

        length = len(str)

        next = [-1 for i in range(length)]


        j = 0
        k = -1



        while j<len(str)-1:
             if k == -1 or str[j] == str[k]:
                j+=1
                k+=1
                next[j] = k
             else:
                 k = next[k]


        return next

s = Solution()
print s.helper("ABCSD","CSD")
# print s.findMaxLength("ABCDABD")
print s.findMaxLength("ABCDABDABF")




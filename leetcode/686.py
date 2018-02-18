
class Solution:
    def helper(self,A,B):
        temp = A
        times = 1
        al = len(A)
        bl = len(B)

        while True:

            #重点在寻找这个终结点
            #如果A的每一个下标都在temp字符串中能够并可能搜索到B字符串
            #如果本次再无法搜索到字符串则不能再搜索到，因为之后的添加也只是重复的A，是没有意义的寻找
            if len(temp) - al >= bl:
                if temp.find(B) != -1:
                    return times
                else:
                    return -1

            #因为B是A的子串，所以当temp的长度大于等于bl时，就应该进行搜索
            if len(temp) >= bl:
                if temp.find(B) != -1:
                    return times

            times += 1
            temp += A

s = Solution()
print(s.helper("abcabcabcabc","abac"))

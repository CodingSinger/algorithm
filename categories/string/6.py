class Solution:

    # 思路:构造一个numRows长度的字符串数组，将原字符串从上到下从下到上插入这个数组相应的下标的字符串。
    def helper(self, s, numRows):

        list = [[] for i in range(numRows)]
        i, reverse,finish = 0, False,False
        while not finish:
            if not reverse:
                for row in range(numRows):
                    if i >=len(s):
                        finish = True
                        break
                    list[row].append(s[i])
                    i += 1
            else:
                for row in range(numRows-2, 0, -1): #需要注意反向插入的时候range的边界
                    if  i>=len(s):
                        finish = True
                        break
                    list[row].append(s[i])
                    i += 1
            reverse = not reverse

        res = ""
        for s in list:
            res+="".join(s)
        return res

s = Solution()
print(s.helper("PAYPALISHIRING",3))
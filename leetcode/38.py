


#思路 :典型的字符串序列处理题目 因为每个n的所求序列都依赖于n-1的结果，所以解题过程一定需要保存上一步的结果
class Solution:
    def helper(self,n):

        if n == 2:
            return "11"
        if n == 1:
            return "1"
        step = "11"
        temp = ""
        count = 1
        for i in range(3,n+1):

            temp = step
            step = ""
            for k in range(len(temp)-1): #因为k+1的原因 所以这里只能遍历到   [0~len-1)
                if temp[k+1] == temp[k]:
                    count +=1
                else:
                    step += str(count)+temp[k]
                    count = 1


            k+=1 #因为只遍历到[0~len-1]的原因 而无论最后一个元素等不等于倒数第二个元素，都没有将temp的最后一个元素的计数连接上去 所以在收尾的地方继续连接
            step += str(count)+temp[k]
            count = 1





        return step


s = Solution()
print s.helper(6)

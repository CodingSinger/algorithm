


# 思路很清晰 ：计算每两个相邻1之间的0个数empty，种植花数和empty关系为 f = (empty-1)//2 ,但是要额外考虑一头一尾的情况，如[0,0,1,0,0,0,1,0,0] 头尾情况的0的个数并不满足之前公式，因此为了统一处理，
#在头尾处各加上[1,0]和[0,1]
class Solution:
    def helper(self,flowerbed,n):
        flowerbed += [0,1]
        flowerbed = [1,0]+flowerbed
        last = -1
        sum = 0
        for i,num in enumerate(flowerbed):
            if num == 1:
                current = i
                empty = current-last-1
                last = current
                if empty <=1:
                    continue
                sum += (empty-1) //2

        return sum>=n


s = Solution()
print((-1)//2)
l = [1,0,1,0,1,0,1]
print(s.helper(l,0))


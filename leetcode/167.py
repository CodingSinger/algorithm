

class Solution:
    def helper(self,numbers,target):




        two = len(numbers)-1
        one = 0

        result = []

        while one <= two:


            if numbers[one]+numbers[two] > target:

                two-=1





            elif numbers[two]+numbers[one] <target:
                one+=1




            else:

                result.append(one+1)
                result.append(two+1)
                return result

        return result


#当偏大时 则有两种决策：
    # 1.高值two左移 高值two = (上一次高值+本次高值)/2 即取中间值
    # 2. 低值one左移 one = (上一次低值+本次低值)/2
# 同理 偏大时也有两种决策
# 如上决策都要满足two >one 
    def helper1(self,numbers,target):


        two = low2 = len(numbers)-1
        one = high2= 0

        high2 = 0

        result = []

        while one <= two:




            if numbers[one]+numbers[two] > target:




                if two != one+1:

                    high2 = high
                    high = two #保存上一次高值


                    two = (int)((high2+two)/2)
                else:
                    low2 = low

                    low = one

                    one = (int)((low2+one)/2)

            elif numbers[two]+numbers[one] <target:
                if two +1 == len(numbers)-1:

                    two = (int)((len(numbers)-1+two))
                else:



                two = low

                low = one
                one = (int)((one+two)/2)
            else:

                result.append(one+1)
                result.append(two+1)
                return result
        return result



s = Solution()
print(s.helper([2,7,11,15,18],25))
print(s.helper1([2,7,11,15,18],25))
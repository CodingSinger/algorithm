class Solution:
    def helper(self,N):



        valid = 0
        for i in range(N+1):
            s = str(i)

            flag = True
            for k in s:
                if k in '347':
                    flag = False

                    break
            if flag:
                for k in s:
                    if k in '2569':
                        valid +=1
                        break

        return valid
s = Solution()

print([1,3])
print(iter([1,3]))
l = [x for x in range(10)] #x为l中的元素
print(l)
l1 = [d not in '234' for d in '23d45'] # d not in '234'为l1中的元素
print(l1)
print(all(d not in '234' for d in '23d45'))


d = 'ds'


print()



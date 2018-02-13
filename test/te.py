

class Solution:

    def __init__(self):
        self.nums = []
        self.nums.append(2)
        self.nums.append(3)
        self.nums.append(4)
        print(self.nums)
        self.nums[2] = 10



arr = [1,2,3,4]
arr1 = arr[0:2]

print(arr1)
arr1[1] = 3
print(arr1)
print(arr)
s = Solution()
print(s.nums)

s1 = "sassd"
print(s1[:-1])

s2 = [[],[2],[3],[]]

print(s2.reverse())

c1 = [[2,3],[3,2],[4,4]]

c2= c1.copy()

print(c2)
c1[2][1] = 8
print(c2)
print(c1)

for i in range(-1,0,1):
    print(i)
print(i)
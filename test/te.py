

# class Solution:
#     #
#     # def __init__(self):
#     #     self.nums = []
#     #     self.nums.append(2)
#     #
#     #     self.nums.append(4)
#     #     print(self.nums)
#     #     self.nums[2] = 10
#
# l1 = [1 if i%2 ==0 else 0 for i in range(10)]
# a = range(10)
# print(a)
# a[1]=20
# print(l1)
# li = [1,3,5,7,9]
# #不建议在循环中改变当前正在循环的数组 https://www.zhihu.com/question/49098374
# for i in li:
#     print(i)
#     li.remove(i)
# for i in range(0,1):
#     print("dd")
# i,j = 1,2
# i,j = j,i
# print(i,j)
print(10/3)
print(10//3)
list = [1,2,3]
list1 = list
list1[1] = 6
print(list)
arr2 = [1,2,3,4]
# arr2[0:2] = [5,6]
arr3 = arr2[:2]
arr3[0] = 10
print(arr2)
print(arr3)
print("test")
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
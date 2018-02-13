
#coding=utf-8
class Solution:
    def helper(self,letters,target):

        for letter in letters:
            if letter>target:
                return letter
        return letters[0]
        #如果没有结果则说明target是最大的，但是因为是回环的，所以，最小的就是结果
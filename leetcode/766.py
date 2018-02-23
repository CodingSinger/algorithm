

class Solution:
    #思路 统一对角线上的元素行列差相等 所以可以通过判断行列差相等的元素是否相同
    def helper(self,matrix):
       map = {}
       for r,es in enumerate(matrix):
           for c,e in enumerate(es):
               if r-c not in map:
                   map[r-c] = e
               elif map[r-c] != e:
                   return False
       return True

    # 思路：因为对角线上的下一个元素的坐标为(r-1,c-1)所以 判断临近元素是否相等 不等则直接返回false
    def helper2(self,matrix):

        for r,es in enumerate(matrix):
            for c,e in enumerate(es):
                if r == 0 or c == 0 or matrix[r-1,c-1] == e:
                    pass
                else:
                    return False
        return True


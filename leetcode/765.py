class Solution:
    def helper(self, row):

        pos, count = {}, 0
        for i in row:
            pos[row[i]] = i

        for i in range(0, len(row), 2):
            if row[i] // 2 == row[i + 1] // 2: #夫妻除以2取整应该都相等
                continue
            else:#不是夫妻

                other = row[i]+1 if row[i] % 2 == 0 else row[i]-1 #获得另一半的数值
                # 定位另一半在row中的索引
                d = pos[other]
                pos[other], pos[row[i + 1]] = i + 1, d #交换之后更新pos   other移到i+1的位置，row[i+1]移到d的位置， other:i+1,row[i+1]:d
                row[i + 1], row[d] = other, row[i + 1] #进行交换 row[i+1]和另一半
                count += 1
        print(row)
        return count


s = Solution()
print(s.helper([0, 3, 4, 1, 2, 5, 6, 8, 7, 9]))

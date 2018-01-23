

# 举个例子，例如数组大小是 100，比它大的最小斐波那契数是 144。
#
# 斐波那契数列如下：0 1 1 2 3 5 8 13 21 34 55 89 144
#
# 我们记 F(n) = 144,F(n-1) = 89, F(n-2) = 55。
#
# 我们先查看第 0 + F(n-2) 个数，如果比关键值小则直接将范围缩小到 [55, 100]；否则则在[0, 55]之间查找。
#
# 之后我们令 n = n-1。
def process(x,key):
    length = len(x)

    fk_1 = 1
    fk_2 = 0
    fk = fk_1+fk_2
    while fk<length:
        fk_2 = fk_1
        fk_1 = fk
        fk = fk_1+fk_2



    index = fk_2
    low = 0
    while fk_2 > 0 :

        index = length - 1 if low+fk_2 >= length else low+fk_2
        if x[index]<key:
            low = index
        elif key == x[index]:
            return index

        fk = fk_1
        fk_1 = fk_2
        fk_2 = fk-fk_1


if __name__ == '__main__':
    arr = [1,4,5,8,11,23,43]

    print process(arr,43)

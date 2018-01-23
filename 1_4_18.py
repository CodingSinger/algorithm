




def helper(x):
    lenth = len(x)
    if len == 1:
        return 0
    if x[0] < x[1]:
        return 0
    if x[lenth-1]<x[lenth-2]:
        return  lenth-1
    low = 1
    high = lenth-2

    while low<=high:
        mid = (low+high)/2

        if x[mid]<x[mid-1] and x[mid]<x[mid+1]:
            return mid
        elif x[mid-1]>x[mid+1]:
            low = mid+1
        else:
            high = mid-1




    return  -1


if __name__ == '__main__':

    x = [-4,-5,2,7,4,3,5,6]
    print(helper(x))



class Solution:
    # 11 11
    def helper(self,a,b):

        la,lb = len(a),len(b)
        i,k = -1,-1
        added = 0
        result = ""
        r1 = 0
        r2 = 0
        while i>=-la or k>=-lb:

            r1,r2 = 0,0
            if i >= -la:
                r1 = int(a[i])

            if k >= -lb:
                r2 = int(b[k])



            to = r1+r2+added

            if to >=2:
                added = 1
                to = to % 2
            else:
                added = 0
            result = str(to)+result
            i-=1
            k-=1
        if added ==1:
            result = str(added)+result
        return result





s = Solution()
print(s.helper("110010","100"))

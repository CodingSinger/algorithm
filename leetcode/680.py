class Solution:
     def helper(self,s):
         sl = len(s)
         last = sl-1
         start = 0
         final = sl//2

         flag = True
         while start <= final:
             if s[start] != s[last]:
                 if flag:
                     #尝试删除
                    if s[last-1] == s[start]:
                        #删除last
                        last-=1
                    elif s[last] == s[start+1]:
                        #删除i处的字母
                        start+=1
                    else:
                        return False
                    flag = False
                    final = (sl-1)//2

                 else:
                     return False
             start+=1
             last -=1

         return True


     # time limit
     def helper2(self,s):

         if s == s[::-1]:
             return True
         for i in range(len(s)):
             temp = s[:i]+s[i+1:]
             if temp == s[::-1]:
                 return True
         return False


     def helper3(self,s):
         left = 0
         right = len(s)-1

         while left < right:
             if s[left] != s[right]:
                 one,two = s[left:right],s[left+1:right+1] #分别去掉left和去掉right

                 if one == one[::-1] or two == two[::-1]:
                     return True
                 else:
                     return False

             left,right = left+1,right-1
         return True





s = Solution()
print(s.helper("ebcbbececabbacecbbcbe"))
print(s.helper3("ebcbbececabbacecbbcbe"))
str = "sada"
print(str[::-1])
print(str[2:])









class Solution:
    def helper(self,bits):


      index = 0

      length = len(bits)
      while index<length:
          if index == length - 1:
              return True
          if bits[index] == 1:
              index+=2
          else:
              index+=1


      return False

    def helper2(self,bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0




s = Solution()
print(s.helper([1,1,1,0,0]))

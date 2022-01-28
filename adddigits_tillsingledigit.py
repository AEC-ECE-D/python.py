import math
class Solution:
   def solve(self, n):
      if n < 10:
         return n
      s = 0
      l = math.floor(math.log(n, 10) + 1)
      while l > 0:
         s += n % 10
         n //= 10
         l -= 1
      return self.solve(s)
ob = Solution()
print(ob.solve(int(input())))

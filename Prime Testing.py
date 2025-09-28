import math
class Solution:
    def isPrime(self, n):
        # code here
        if n < 2:
            return False
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
               return False
        return True    
                

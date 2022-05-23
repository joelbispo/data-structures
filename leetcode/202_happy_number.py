class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0
        
        while n:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output   
        
#         output = 0
        
#         n_str = str(n)
        
#         for digit in range(len(n_str)):
#             digit = int(digit)**2
#             output += digit
        
#         return output
            
    
        
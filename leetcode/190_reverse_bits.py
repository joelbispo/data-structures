class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1
            
            res = res | ( bit << (31 - i))
            
        return res


    #SOLUTION 2

#         result = 0
        
#         for i in range(32):
#             result = result << 1
            
#             if n%2 == 1:
#                 result += 1
#             n = n >> 1
            
#        return result
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        line = ''
        
        for i in x :
            line = i + line
            
        if line == x:
            return True
        else:
            return False
    
    
solution = Solution()
print(solution.isPalindrome(12))

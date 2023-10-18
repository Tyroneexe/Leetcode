# Longest Common Prefix

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(s) for s in strs)
        
        commonP = ""
        
        for i in range(min_length):
            char = strs[0][i]
            
            if all(s[i] == char for s in strs):
                commonP += char
            else:
                break
        
        return commonP


    
solution = Solution()
# strings = ["dog","racecar","car"]
strings = ["flower","flow","flight"]

print(solution.longestCommonPrefix(strings))
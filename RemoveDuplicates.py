from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = []
        
        for num in nums:
            if num not in new_list:
                new_list.append(num)

        nums[:] = new_list

solution = Solution()
nums = [1, 1, 2, 3]
solution.removeDuplicates(nums)
print(nums)

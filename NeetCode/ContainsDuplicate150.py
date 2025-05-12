from typing import List
# Given an integer array nums, return true if any value appears more than once in the array, 
# otherwise return false
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        
        return False

nums = [1, 2, 3, 3]
sol = Solution()
print(sol.hasDuplicate(nums)) 

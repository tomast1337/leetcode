from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
solution = Solution()
result = solution.hasDuplicate([1, 2, 3, 3])
# print(f"Result: {result}")

"""
count: {3: 2, 1: 1, 2: 1}
Result: True
"""

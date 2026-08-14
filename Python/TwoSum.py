from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in hasher:
                return [hasher[complement], idx]
            hasher[num] = idx


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
resultado = sol.twoSum(nums, target)
print(resultado)
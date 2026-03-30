from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        else:
            start = 2
            for i in range(2,len(nums)):
                if nums[i] != nums[start-2]:
                    nums[start] = nums[i]
                    start += 1
            return start
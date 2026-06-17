class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored = {}
        for i, n in enumerate(nums):
            if target - n in stored:
                return [stored[target-n], i]
            else:
                stored[n] = i
        return []
        
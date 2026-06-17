class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 0
            else:
                return True
        return False
         
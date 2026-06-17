class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = [i]
            else:
                m[nums[i]].append(i)
        for i in range(len(nums)):
            if target - nums[i] in m:
                for v in m[target-nums[i]]:
                    if v != i:
                        return [i, v]

        
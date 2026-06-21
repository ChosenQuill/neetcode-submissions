class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 1
        z = False
        for n in nums:
            if n != 0:
                s *= n
            elif not z:
                z = True
            else:
                return [0] * len(nums)
        res = []
        for n in nums:
            if z:
                if n == 0:
                    res.append(s)
                else:
                    res.append(0)
            else:
                res.append(s // n)
        return res
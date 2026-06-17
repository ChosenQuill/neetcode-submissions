from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        r: list[list[int]] = [[] for _ in range(2000)]
        m = defaultdict(int)
        for n in nums:
            count = m[n]
            if n in r[count]:
                r[count].remove(n)
            count += 1
            r[count].append(n)
            m[n] = count
        res = []
        for i in range(1999, 0, -1):
            if r[i]:
                res.extend(r[i])
            if len(res) >= k:
                return res
        return res


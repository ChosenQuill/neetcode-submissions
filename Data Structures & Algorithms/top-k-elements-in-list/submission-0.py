from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        return [k for v, k in sorted([[v,k] for k, v in m.items()], reverse=True)[:t]]

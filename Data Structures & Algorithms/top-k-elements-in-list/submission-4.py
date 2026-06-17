from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or not nums:
            return []
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(nums), 0, -1):
            if freq[i]:
                res.extend(freq[i])
            if len(res) >= k:
                return res
        return []
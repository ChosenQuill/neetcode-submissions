from collections import defaultdict

class Solution:

    def getSet(self, s: str) -> tuple[tuple[str, int], ...]:
        m: defaultdict[str, int] = defaultdict(int)
        for c in s:
            m[c] += 1
        return tuple(sorted(m.items()))


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store: defaultdict[tuple, list] = defaultdict(list)
        for s in strs:
            store[self.getSet(s)].append(s) 
        return list(store.values())
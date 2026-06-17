class Solution:
    def getMap(self, s: str) -> dict[str, int]:
        res = {}
        for c in s:
            res[c] = res.get(c, 0) + 1
        return res
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            so = str(sorted(s))
            l = store.get(so, [])
            l.append(s)
            store[so] = l
        
        res = []
        return [v for v in store.values()]
        

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        pos = 0
        res = []
        while pos < len(s):
            new = s.find("#", pos)
            l = int(s[pos:new])
            pos = new + 1
            res.append(s[pos:pos + l])
            pos += l
        return res


class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(len(strs)) + "," + ",".join(str(len(s)) for s in strs) + "," + "".join(strs)
        


    def decode(self, s: str) -> List[str]:
        pointer = s.find(",")
        count = int(s[:pointer])
        lengths = []
        for _ in range(count):
            new = s.find(",", pointer + 1)
            lengths.append(int(s[pointer+1:new]))
            pointer = new
        res = []
        pointer += 1
        for l in lengths:
            res.append(s[pointer:pointer + l])
            pointer += l
        return res

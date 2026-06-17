class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return ":".join(s.encode("utf-8").hex() for s in strs)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return [bytes.fromhex(n).decode("utf-8") for n in s.split(":")
]
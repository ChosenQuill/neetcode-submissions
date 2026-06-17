class Solution:

    def encode(self, strs: List[str]) -> str:
        return ":".join(s.encode("utf-8").hex() for s in strs)
    def decode(self, s: str) -> List[str]:
        return [bytes.fromhex(n).decode("utf-8") for n in s.split(":")
]
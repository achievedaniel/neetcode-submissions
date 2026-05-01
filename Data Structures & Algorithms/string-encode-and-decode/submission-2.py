class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        ind = ""
        while i <= len(s) -1:
            if s[i].isdigit():
                ind += s[i]
                i += 1
            else:
                ind = int(ind) + i
                result.append(s[i + 1: ind + 1])
                i = ind + 1
                ind = ""
        return result

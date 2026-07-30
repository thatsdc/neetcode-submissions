class Solution:

    DELIMITER = "è"

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs: 
            encoded += f"{s}{self.DELIMITER}"

        return encoded

    def decode(self, s: str) -> List[str]:

        result = []
        word = ""
        for c in s: 
            if c != self.DELIMITER:
                word += c
            else: 
                result.append(word)
                word = ""

        return result


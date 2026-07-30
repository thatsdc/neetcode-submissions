class Solution:

    DELIMITER = "*$"

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs: 
            encoded += f"{s}{self.DELIMITER}"

        return encoded

    def decode(self, s: str) -> List[str]:

        result = []
        word = ""
        for c in s: 
            word += c
            
            if word[-2:] == self.DELIMITER:
                result.append(word[:-2])
                word = ""

        return result


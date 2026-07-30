class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs: 
            encoded += f"{len(s)}#{s}"

        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        counter = -1
        word = ""

        number_str = ""

        s += "/"
        for i in range(len(s)): 
            if counter < 1:
                if counter == 0: 
                    result.append(word)
                    word = ""
                    counter = -1 

                if s[i] == "#":
                    counter = int(number_str)
                    number_str = ""
                else: 
                    number_str += s[i]

  
            else: 
                word += s[i]
                counter -= 1

        return result
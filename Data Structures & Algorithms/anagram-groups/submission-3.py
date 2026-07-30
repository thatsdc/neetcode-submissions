class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs: 
            str_sorted = "".join(sorted(list(s)))

            if anagrams.get(str_sorted) is not None:
                anagrams[str_sorted].append(s)
            else:
                anagrams[str_sorted] = [s]

        return list(anagrams.values())
                    
            

        
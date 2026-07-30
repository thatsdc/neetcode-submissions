class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs: 
            str_sorted = "".join(sorted(list(s)))

            found_anagram = False
            for k in anagrams:
                if k == str_sorted:
                    anagrams[str_sorted].append(s)
                    found_anagram = True
            
            if not found_anagram: 
                anagrams[str_sorted] = [s]

        return list(anagrams.values())
                    
            

        
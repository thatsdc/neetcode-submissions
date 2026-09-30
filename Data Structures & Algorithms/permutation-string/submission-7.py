class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a_idx = 0
        b_idx = len(s1)
        def_dict = dict()

        # Fill the dict with s1 characters
        for c in s1: 
            if c not in def_dict: 
                def_dict.update({ c: 1 }) 
            else: 
                def_dict[c] += 1

        # Use a sliding window
        while b_idx < len(s2)+1:
            t_str = s2[a_idx:b_idx]
            temp_dict = dict()

            for c in t_str: 
                if c not in temp_dict: 
                    temp_dict.update({ c: 1 }) 
                else: 
                    temp_dict[c] += 1        

            if temp_dict == def_dict: 
                return True
            else: 
                a_idx += 1
                b_idx += 1

        return False
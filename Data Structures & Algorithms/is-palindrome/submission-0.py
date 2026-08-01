class Solution:
    def isPalindrome(self, s: str) -> bool:
        simp_str = "".join(c.lower() for c in s if c.isalnum())

        for i in range(int(len(simp_str)/2)):
            if simp_str[i] != simp_str[len(simp_str)-1-i]:
                return False

        return True

                    
            


        
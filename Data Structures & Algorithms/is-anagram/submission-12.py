class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n + m)
        if len(s) != len(t): return False
        return sorted(list(s)) == sorted(list(t))
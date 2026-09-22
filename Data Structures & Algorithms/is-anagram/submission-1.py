class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_chars = [char for char in s]
        t_chars = [char for char in t]
        s_chars = sorted(s_chars)
        t_chars = sorted(t_chars)

        if s_chars == t_chars:
            return True
        else:
            return False

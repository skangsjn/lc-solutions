from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # try to map letters
        mpp = {}

        for s_char, t_char in zip(s, t):
            if (s_char not in mpp) and (t_char not in mpp.values()):
                mpp[s_char] = t_char
            elif (s_char not in mpp) and (t_char in mpp.values()):
                return False
            elif (s_char in mpp) and mpp[s_char] != t_char:
                return False
        return True
            

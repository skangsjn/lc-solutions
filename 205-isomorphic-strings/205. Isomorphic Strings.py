from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # try to map letters
        mpp_s = {}
        mpp_t = {}

        for s_char, t_char in zip(s, t):
            if (s_char not in mpp_s) and (t_char not in mpp_t):
                mpp_s[s_char] = t_char
                mpp_t[t_char] = s_char
            elif (s_char not in mpp_s) and (t_char in mpp_t):
                return False
            elif (s_char in mpp_s) and mpp_s[s_char] != t_char:
                return False
        return True
            

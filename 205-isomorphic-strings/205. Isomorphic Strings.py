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
            
            elif (mpp_s.get(s_char) != t_char) or (mpp_t.get(t_char) != s_char):
                return False
        return True
            

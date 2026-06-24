class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split()
        mpp = {}

        if len(pattern) != len(s_arr):
            return False
        
        for c, word in zip(pattern, s_arr):
            if (c not in mpp) and (word not in mpp.values()):
                mpp[c] = word
            elif (c not in mpp) and (word in mpp.values()):
                return False
            elif (c in mpp) and (mpp[c] != word):
                return False

        return True
            
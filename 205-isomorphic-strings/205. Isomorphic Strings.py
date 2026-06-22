from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dic = defaultdict(list)
        t_dic = defaultdict(list)

        for i in range(len(s)):
            s_dic[s[i]].append(i)
        for i in range(len(t)):
            t_dic[t[i]].append(i)

        return sorted(s_dic.values()) == sorted(t_dic.values())
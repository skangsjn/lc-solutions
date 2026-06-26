from collections import defaultdict, Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        shared = defaultdict(int)
        s_only = []
        ans = []

        for i in range(len(s)):
            if s[i] in order:
                shared[s[i]] += 1
            else:
                s_only.append(s[i])
        
        for j in range(len(order)):
            if order[j] in shared:
                ans.append(order[j] * shared[order[j]])
        
        print(shared)
        # print(s_only)
        
        # print(ans)
        return ''.join(ans + s_only)
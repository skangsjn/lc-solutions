from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        count1 = Counter(word1)
        count2 = Counter(word2)

        if count1.keys() != count2.keys():
            return False

        # print(count1.values())
        # print(count2.values())

        # print(count1.values() == count2.values())
        return sorted(count1.values()) == sorted(count2.values())
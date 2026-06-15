class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = 0 
        r = len(s) - 1
        arr = list(s)

        while l < r:
            if not s[l].isalpha():
                l += 1
            if not s[r].isalpha():
                r -= 1

            if s[l].isalpha() and s[r].isalpha():
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        
        return ''.join(arr)
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         idx = 0 
#         stack = []
#         ans = []

#         while idx < len(word):
#             stack.append(word[idx])
#             if word[idx] == ch:
#                 while stack:
#                     ans.append(stack.pop())
#                 idx += 1
#                 while idx < len(word):
#                     ans.append(word[idx])
#                     idx += 1
#                 return ''.join(ans)
#             idx += 1
        
#         return word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = list(word)
        l = 0

        for r in range(len(arr)):
            if arr[r] == ch:
                while l < r:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
                return ''.join(arr)
        return word

        
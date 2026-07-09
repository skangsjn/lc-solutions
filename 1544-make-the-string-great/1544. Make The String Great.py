class Solution:
    def makeGood(self, s: str) -> str:

        def same_letter_diff_case(c1, c2):
            return c1.lower() == c2.lower() and c1 != c2

        stack = []
        for c in s:
            if stack and same_letter_diff_case(c, stack[-1]):
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_arr = path.split('/')

        for folder in path_arr:
            if folder == '..':
                if stack:
                    stack.pop()
            elif folder == '.' or not folder:
                continue
            else:
                stack.append(folder)
        
        return '/' + '/'.join(stack)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_arr = path.split('/')

        for folder in path_arr:
            if stack and folder == '..':
                stack.pop()
            
            if folder not in ('.', '..', ''):
                stack.append(folder)
        
        return '/' + '/'.join(stack)
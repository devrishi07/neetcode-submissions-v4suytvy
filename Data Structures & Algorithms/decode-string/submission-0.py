class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        front = []

        i = 0
        while i < len(s) and not s[i].isdigit():
            front += s[i]
            i += 1

        while i < len(s):

            if s[i] == ']':
                t = ""

                while stack[-1] != '[':
                    t = stack.pop() + t
                stack.pop()
                
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                    
                t = t * int(num)

                stack.extend([c for c in t])

            else:
                stack.append(s[i])
            i += 1
        
        return "".join(front) + "".join(stack)
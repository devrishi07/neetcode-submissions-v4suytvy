class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if ast < 0:
                while stack and stack[-1] > 0 and abs(ast) > stack[-1]:
                    stack.pop()
                if not stack:
                    stack.append(ast)
                else:
                    if stack[-1] < 0:
                        stack.append(ast)
                    else:
                        if stack[-1] == abs(ast):
                            stack.pop()
            else:
                stack.append(ast)
        
        return stack

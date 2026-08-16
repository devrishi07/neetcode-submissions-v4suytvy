class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        score = 0

        for op in ops:
            if self.is_int(op):
                score += int(op)
                stack.append(int(op))

            elif op == "C":
                score -= stack.pop()
            
            elif op == "+":
                new = stack[-1] + stack[-2]
                score += new
                stack.append(new)
            
            elif  op == "D":
                new = 2 * stack[-1]
                score += new 
                stack.append(new)
        
        return score

    def is_int(self, val):
        try:
            int(val)
            return True
        except ValueError:
            return False
                




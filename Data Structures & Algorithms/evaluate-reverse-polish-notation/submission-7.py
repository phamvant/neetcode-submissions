class Solution:
    def op(self, l, r, sym):
        l, r = int(l), int(r)
        match sym:
            case "+":
                return l + r
            case "-":
                return l - r
            case "*":
                return l * r
            case "/":
                return l / r

    def evalRPN(self, tokens: List[str]) -> int:
        self.numStack = []
        ops = set(["+", "-", "*", "/"])
        
        for t in tokens:
            if len(self.numStack) > 1 and t in ops:
                r = self.numStack.pop()
                l = self.numStack.pop()
                self.numStack.append(self.op(l, r, t))
            else:
                self.numStack.append(t)
        
        return int(self.numStack[0])
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in '+-*/':
                stack.append(tokens[i])
            else:
                x = stack[-2],tokens[i],stack[-1]
                stack.pop()
                stack.pop()
                x = eval(''.join(x))
                stack.append(str(x).split('.')[0])
                
        
        return int(str(eval(''.join(stack))).split(',')[0])
                
        
        
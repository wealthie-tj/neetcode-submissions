class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                result = stack[-2] + stack[-1]
                stack.append(result)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                result = stack[-1] * 2
                stack.append(result)
            else:

                stack.append(int(op))
        print(stack)
        return sum(stack)

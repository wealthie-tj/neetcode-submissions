class Solution:
    def calPoints(self, operations: List[str]) -> int:

        ops = ['+', 'C', 'D']

        record = []
        for op in operations:
            if op=='+':
                numA = record[-1]
                numB = record[-2]
                res = numA + numB
                record.append(res)
            elif op=='C':
                record.pop()
            elif op=='D':
                res = record[-1] * 2
                record.append(res)
            else:
                record.append(int(op))
        
        return sum(record)
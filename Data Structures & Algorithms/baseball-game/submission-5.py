class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        finalRes = 0
        for op in operations:
            if op=='+':
                numA = record[-1]
                numB = record[-2]
                res = numA + numB
                record.append(res)
                finalRes += res
            elif op=='C':
                res = record.pop()
                finalRes -= res
            elif op=='D':
                res = record[-1] * 2
                record.append(res)
                finalRes += res
            else:
                record.append(int(op))
                finalRes += int(op)
        
        return finalRes
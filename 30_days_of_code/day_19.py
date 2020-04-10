class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum([k for k in range(1, n//2+1) if n % k == 0]) + n

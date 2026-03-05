class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        multi = 1
        for i in str(n):
            digit = int(i) 
            add += digit
            multi *= digit
            
        return multi - add
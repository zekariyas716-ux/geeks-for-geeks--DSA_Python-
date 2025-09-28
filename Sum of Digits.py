class Solution:
    def sumOfDigits(self, n):
        # code here
        lst = []
        for i in str(n):
            lst.append(int(i))
        return sum(lst)

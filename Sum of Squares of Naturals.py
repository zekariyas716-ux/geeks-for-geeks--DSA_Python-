class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, n):
        return n * (n + 1) * (2 * n + 1) // 6   

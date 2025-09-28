class Solution:
    def getTable(self,n):
        # code here
        table =[]
        i = 1
        while i < 11:
            table.append(n*i)
            i += 1
        return table
        

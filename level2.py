class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A== 1:
            return [[1]]
        if A== 0:
            return []
        center = (A-1, A-1) #center is always 1
        result = []

        for i in range(0,A):
            row = []
            for j in range(0,A):
                row.append(int(max(math.fabs(center[0]-i), math.fabs(center[1]-j)))+1)
            for k in range(A-2,-1,-1):
                row.append(row[k])
            result.append(row)
        for x in range(A-2,-1,-1):
            i = i+1
            result.append(result[x])

        return result

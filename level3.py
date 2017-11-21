class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
        if A is None:
            return 0
        if B > C or C<=0:
            return 0
        result = 0
        #print('B:'+str(B)+' C:'+str(C))
        for i in range(len(A)):
            #print('ith:'+str(i)+' A[i]:'+str(A[i]))
            if  A[i]<=C:
                #print('A[i]:'+str(A[i]))
                sub = A[i]
                #print('A[i]:'+str(A[i])+'at i:'+str(i))
                if A[i]>=B and A[i]<=C:
                    result = result +1
                for j in range(i+1, len(A)):
                    sub = sub + A[j]
                    if sub>=B and sub<=C:
                        #print('A[i]:'+str(A[i])+' A[j]:'+str(A[j])+' at j:'+str(j)+' sub:'+str(sub))
                        result = result + 1
                        #if result > 70 and result <= 80:
                            #print('Found sub:A[i]:'+str(A[i])+' A[j]:'+str(A[j])+' sub sum: '+str(sub)+' result:'+str(result))
                    elif sub > C:
                        break
                '''
                if sub>=B and sub<=C:
                    result = result + 1
                    print('After iter Found sub:A[i]:'+str(A[i])+' A[j]'+str(A[j])+' sub sum: '+str(sub)+' result:'+str(result))
                '''
        #print('final result:'+str(result))
        return result

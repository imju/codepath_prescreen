class Solution:

    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if A is None:
            return 0
        if len(A) == 1:
            return 1
        hash_dc ={}
        for a in A:
            hash_dc[a] = a
        max_l = 1
        cur_l = 1
        for key, vale in sorted(hash_dc.items()):
            #print('key:'+str(key)+' hash_dc:'+str(hash_dc.get(key+1)))
            next = key+1
            if hash_dc.get(next) is not None:
                cur_l+=1
                if cur_l > max_l:
                    max_l = cur_l
                    #print('max_l:'+str(max_l)+' cur_l:'+str(cur_l)+' key:'+str(key))
            else:
                cur_l = 1

        return max_l

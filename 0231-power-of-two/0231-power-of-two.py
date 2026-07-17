class Solution(object):
    def isPowerOfTwo(self,n):
        """
        :type digits: List[int]
        :rtype: int
        """
        if n==1:
            return True
        if n<=0 or n%2!=0:
            return False
        return self.isPowerOfTwo(n//2)
     
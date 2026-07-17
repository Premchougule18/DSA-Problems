class Solution(object):
    def fib(self, n):
        """
        :type digits: List[int]
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n>1:
            return self.fib(n-1)+ self.fib(n-2)       
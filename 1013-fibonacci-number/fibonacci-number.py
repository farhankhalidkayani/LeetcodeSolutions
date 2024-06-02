class Solution:
    def fib(self, n: int) -> int:
        memorize={0:0,1:1}
        def f(x):
            if x in memorize:
                return memorize[x]
            else:
                memorize[x]=f(x-1)+f(x-2)
                return memorize[x]
        return f(n)
        
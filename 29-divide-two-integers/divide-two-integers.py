import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res=dividend/divisor
        if res<=0:
            res=math.ceil(res)
        if res>0:
            res=math.floor(res)
        if res>(2**31)-1:
            return (2**31)-1
        if res<-2**31:
            return -2**31
        return res
        
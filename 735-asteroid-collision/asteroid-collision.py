class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for ass in asteroids:
            while res and res[-1]>0 and ass<0:
                if res[-1]==-ass:
                    res.pop()
                    break
                elif res[-1] < -ass:
                    res.pop()
                    continue
                else:
                    break
            else:
                res.append(ass)
            
            
        return res
        
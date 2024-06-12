class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hashtables={n:i for i,n in enumerate(s)}
        hashtablet={n:i for i,n in enumerate(t)}
        res=0
        for c in hashtables:
            res+=(abs(hashtables[c]-hashtablet[c]))
        return res

        
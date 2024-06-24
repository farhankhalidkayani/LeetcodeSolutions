class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!= len(word2):
            return False
        hashtable1=Counter(word1)
        hashtable2=Counter(word2)
        return set(hashtable1.keys())==set(hashtable2.keys()) and sorted(hashtable1.values())== sorted(hashtable2.values())
        
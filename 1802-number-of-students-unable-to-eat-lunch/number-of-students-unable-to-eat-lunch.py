class Solution(object):
    def countStudents(self, students, sandwiches):
        result=len(students)
        hashtable=Counter(students)
        for c in sandwiches:
            if hashtable[c]>0:
                result-=1
                hashtable[c]-=1
            else:
                return result
        return result
        
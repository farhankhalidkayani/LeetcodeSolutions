from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students=deque(students)
        sandwiches=deque(sandwiches)
        count=0
        while len(students)!=0 and count!=len(students):
            if(students[0]==sandwiches[0]):
                students.popleft()
                sandwiches.popleft()
                count=0
            
            else:
                student= students.popleft()
                students.append(student)
                count+=1
        return len(students)
            
        
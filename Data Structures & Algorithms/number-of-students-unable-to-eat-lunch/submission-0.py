class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        notFound = False
        studentPointer = 0
        loopBackPointer = 0
        while len(sandwiches) > 0 and notFound == False:
            notFound = True
            if students[studentPointer] == sandwiches[0]:
                students.pop(studentPointer)
                sandwiches.pop(0)
                if len(students) > 0:
                    studentPointer = studentPointer % len(students)
                loopBackPointer = studentPointer
                notFound = False
            else:
                studentPointer = (studentPointer + 1) % len(students)
                if studentPointer == loopBackPointer:
                    break
                notFound = False


        return len(sandwiches)
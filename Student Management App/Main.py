'''
Write an application that manages lab assignments for students at a given discipline. The application will store: 
 Student: <studentID>, <name>, <group>. 
 Assignment: <assignmentID>,  <description>, <deadline>. 
 Grade: <assignmentID>, <studentID>, <grade>. 
Create an application that allows to: 

1. Manage the list of students and available assignments. 
The application must allow the user to add, remove, update, and list both students and assignments.  

2. Give assignments to a student or a group of students (unless already given). 
In case an assignment is given to a group of students, every student in the group will receive it. 
In case there exist students who were previously given that assignment, it will not be assigned again. 

3. Grade student for a given assignment. 
When grading, the program must allow the user to select the assignment that is graded, from the student’s list of ungraded assignments.  
A student’s grade for a given assignment cannot be changed. 
Deleting a student removes their assignments. Deleting an assignment also removes all grades at that assignment. 

4. Create statistics:  
o All students who received a given assignment, ordered alphabetically or by average grade for that assignment. 
o All students who are late in handing in at least one assignment.
    These are all the students who have an ungraded assignment for which the deadline has passed.
o Students with the best school situation, sorted in descending order of the average grade received for all assignments. 
o All assignments for which there is at least one grade, sorted in descending order of the average grade received by all students who received that assignment. 

5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. 
Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying). 
'''
from Repository.Repository import Repository
from Repository.StudentBinaryRepository import StudentPickleFileRepository
from Repository.StudentCSVRepository import StudentCSVFileRepository
from Tests.Tests import Test
from Validators.Validators import gradeValidator, studentValidator, assigValidator
from Controllers.Controllers import studentController, assignmentController, gradeController
from UI.Console import Console

t=Test()
t.runTests()

#repoStudents = Repository()
#repoStudents = StudentPickleFileRepository()
repoStudents = StudentCSVFileRepository()

repoAssignments = Repository()
repoGrade = Repository()

gradeValid = gradeValidator()
studentValid = studentValidator()
assigValid = assigValidator()

studentCtrl = studentController(repoStudents,studentValid)
assigCtrl = assignmentController(repoAssignments, assigValid)
gradeCtrl = gradeController(repoGrade,repoStudents, gradeValid)

console=Console(studentCtrl,assigCtrl,gradeCtrl)
console.run()
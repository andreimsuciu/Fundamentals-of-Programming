from Models.Entities import Student, Assignment, Grade
from Errors.Errors import GradingError



class studentController(object):
    
    
    def __init__(self, __repoStudents, __validatorStudents):
        self.__repoStudents = __repoStudents
        self.__validatorStudents = __validatorStudents
    
    def addStudent(self,ident,name,group):
        student = Student(ident,name,group)
        self.__validatorStudents.validateStudent(student)
        self.__repoStudents.add(student)
    
    def removeStudent(self,ident):
        removeStudent = Student(ident,None,None)
        self.__repoStudents.remove(removeStudent)
    
    def updateStudent(self,ident,name,group):
        updatedStudent= Student(ident,name,group)
        self.__validatorStudents.validateStudent(updatedStudent)
        self.__repoStudents.update(updatedStudent)
        
    def getAllStudents(self):
        return self.__repoStudents.getAll()
    
class assignmentController(object):
    
    
    def __init__(self, __repoAssig, __validatorAssig):
        self.__repoAssig = __repoAssig
        self.__validatorAssig = __validatorAssig
    
    def addAssignment(self,ident,desc,deadl):
        assig = Assignment(ident,desc,deadl)
        self.__validatorAssig.validateAssig(assig)
        self.__repoAssig.add(assig)
    
    def removeAssignment(self,ident):
        removedAssig = Assignment(ident,None,None)
        self.__repoAssig.remove(removedAssig)
        
    def updateAssignment(self,ident,desc,deadl):
        updatedAssig= Assignment(ident,desc,deadl)
        self.__validatorAssig.validateAssig(updatedAssig)
        self.__repoAssig.update(updatedAssig)
        
    def getAllAssigs(self):
        return self.__repoAssig.getAll()
    
class gradeController(object):
    '''
    2. Give assignments to a student or a group of students (unless already given). 
In case an assignment is given to a group of students, every student in the group will receive it. 
In case there exist students who were previously given that assignment, it will not be assigned again.
__assignmentID, __studentID, __grade
    '''
    def __init__(self, __repoGrade, __repoStudents, __validatorGrade):
        self.__repoGrade = __repoGrade
        self.__validatorGrade = __validatorGrade
        self.__repoStudents = __repoStudents
        
    def getAllGrades(self):
        return self.__repoGrade.getAll()
    
    def addGrade(self,assigID,studentID,grade):
        gradeOBJ= Grade(assigID,studentID,grade)
        self.__validatorGrade.validateIDs(gradeOBJ)
        self.__validatorGrade.validateGrade(gradeOBJ)
        self.__repoGrade.update(gradeOBJ)
        
    def giveAssigStudent(self,assigID,studentID):
        '''
        Function that gives an assignment to a student, if it has not already been given
        in:assigID, studentID-int
        out:repoGrade - list, with the newly added Assignemnt 
        '''
        grade=Grade(assigID,studentID,0)
        self.__validatorGrade.validateIDs(grade)
        
        gradeList=self.getAllGrades()
        self.__validatorGrade.vallidateID(assigID,gradeList)
        
        self.__repoGrade.add(grade)
    
    def giveAssigGroup(self,assigID,group):    
        gradeList=self.getAllGrades()
        self.__validatorGrade.vallidateID(assigID,gradeList)
        
        for student in self.__repoStudents:
            if group==Student.get_group(student):
                studentID=Student.get_id(student)
                grade=Grade(assigID,studentID,0)
                self.__repoGrade.add(grade)
    
    def gradeAssig(self, assigID,studentID,grade):
        
        for i in self.__repoGrade:
            if assigID==Grade.get_assignmentID(i) and studentID==Grade.get_studentID(i):
                if Grade.get_grade(i) == 0:
                    self.addGrade(assigID, studentID, grade)
                    break
                else:
                    raise GradingError("Assignment already graded!\n")
            else:
                raise GradingError("The given IDs do not match!\n")
    
    def showUngraded(self,studentID):
        
        for i in self.__repoGrade:
            if studentID==Grade.get_studentID(i):
                if Grade.get_grade(i) == 0:
                    print (str(i))
                    
    def removeStudent(self,ident):
        for i in self.__repoGrade[:]:
            if ident==Grade.get_studentID(i):
                self.__repoGrade.remove(i)
    
    def removeAssig(self,ident):
        for i in self.__repoGrade[:]:
            if ident==Grade.get_assignmentID(i):
                self.__repoGrade.remove(i)
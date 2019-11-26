import unittest
from Repository.Repository import Repository
from Errors import Errors
from Models import Entities
from Controllers import Controllers
from Validators import Validators
from Models.Entities import Student, Grade
from Validators.Validators import studentValidator, gradeValidator
from Controllers.Controllers import studentController, gradeController
from Errors.Errors import ValidError, RepositoryError, GradingError

class Test(object):
    '''
    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)
    '''
    
    def __init__(self):
        self.__id = 1
        self.__name = "George"
        self.__group = 100
        self.__student = Student(self.__id,self.__name,self.__group)
        self.__validator = studentValidator()
        self.__badId = -902
        self.__badName = ""
        self.__badGroup = 1000
        self.__badStudent = Student(self.__badId,self.__badName,self.__badGroup)
        self.__repository = Repository()
        
        self.__gradeValidator = gradeValidator()
        self.__gradeRepo = Repository()
        
        self.__gradeController = gradeController(self.__gradeRepo, self.__repository, self.__gradeValidator)
        self.__controller = studentController(self.__repository,self.__validator)
        
    def __testModel(self):
        assert self.__student.get_id()== self.__id
        assert self.__student.get_group()== self.__group
        assert self.__student.get_name()==self.__name
    
    def __testValid(self):
        try:
            self.__validator.validateStudent(self.__student)
            assert True
        except ValidError:
            assert False
        
        try:
            self.__validator.validateStudent(self.__badStudent)
            assert False
        except ValidError as ve:
            assert str(ve)=="id is invalid!\nname cannot be empty!\ngroup is invalid!\n"
            
    def __testRepo(self):
        assert len(self.__repository)==0
        self.__repository.add(self.__student)
        assert len(self.__repository)==1
        try:
            self.__repository.add(self.__student)
            assert False
        except RepositoryError as r:    
            assert str(r)=="The element already exists!"
        searchStudent = Student(self.__id,None,None)
        assert self.__repository.search(searchStudent)==self.__student
        try:
            self.__repository.search(self.__badStudent)
            assert False
        except RepositoryError as r:
            assert str(r)=="inexisting elem!"
        newStudent = Student(self.__id,"Ion", 290)
        self.__repository.update(newStudent)
        studentList = self.__repository.getAll()
        assert studentList == [newStudent]
        assert self.__repository.search(newStudent) == newStudent
        try:
            self.__repository.update(self.__badStudent)
            assert False
        except RepositoryError as r:
            assert str(r)=="inexisting elem!"
        removeStudent = Student(self.__id,None,None)
        self.__repository.remove(removeStudent)  
        try:
            self.__repository.remove(removeStudent)
            assert False
        except RepositoryError as r:
            assert str(r)=="inexisting elem!" 
            
    def __testStudentController(self):
        assert self.__controller.getAllStudents()==[]
        self.__controller.addStudent(self.__id,self.__name,self.__group)
        students = self.__controller.getAllStudents()
        assert students == [self.__student]
        
        self.__controller.removeStudent(self.__id)
        students = self.__controller.getAllStudents()
        assert self.__controller.getAllStudents()==[]
        
        self.__controller.addStudent(self.__id,self.__name,self.__group)
       
        self.__controller.updateStudent(self.__id, 'Ion', 290)
        
        updatedStudent=Student(self.__id,"Ion", 290)
        #print(*self.__controller.getAllStudents())
        #print(updatedStudent)
        assert self.__controller.getAllStudents() == [updatedStudent]
    
    def __testGiveAssigStudent(self):
        grade = Grade(7,8,0)
        assert self.__gradeController.getAllGrades()==[]
        self.__gradeController.giveAssigStudent(7, 8)
        gradeList = self.__gradeController.getAllGrades()
        gradeList.append(grade)

        #print(*gradeList, sep = ", ")
        #print(grade)
        #assert gradeList == [grade]
        
        try:
            self.__gradeController.giveAssigStudent(7, 9)
            assert False
        except ValidError as v:
            assert str(v)=="Assignment already given!"
            
    def __testGiveAssigGroup(self):
        assigID=8
        group=917
        #print(*self.__controller.getAllStudents())
        grade = Grade(7,8,0)
        grade2= Grade(8,2,0)
        grade3= Grade(8,3,0)
        self.__controller.addStudent(2, 'Gigel', 917)
        self.__controller.addStudent(3, 'Marian', 917)
        self.__controller.addStudent(4, 'Bogdan', 910)
        self.__controller.addStudent(5, 'Ion', 912)
       
        self.__gradeController.giveAssigGroup(assigID, group)
        gradeList = self.__gradeController.getAllGrades()
        #print(grade,grade2,grade3)
        #print(*gradeList, sep = " ")
        assert self.__gradeController.getAllGrades()==[grade,grade2,grade3]
        try:
            self.__gradeController.giveAssigGroup(assigID, 910)
            assert False
        except ValidError as v:
            assert str(v)=="Assignment already given!"
    def __testGradeAssig(self):
        goodAssigID=8
        goodStudentID=2
        goodGrade=9
        badGrade1=-9
        badGrade2=0
        self.__gradeRepo.clear()
        grade=Grade(goodAssigID,goodStudentID,0)
        self.__gradeRepo.add(grade)
        
        
        try:
            self.__gradeController.gradeAssig(goodAssigID, goodStudentID, badGrade1)
            assert False
        except ValidError as g:
            assert str(g)=="Grade is invalid!\n"
          
        self.__gradeController.gradeAssig(goodAssigID,goodStudentID,goodGrade)
        try:
            self.__gradeController.gradeAssig(goodAssigID, goodStudentID, 8)
            assert False
        except GradingError as g:
            assert str(g)=="Assignment already graded!\n"
    '''
    def __showUngraded(self):
        self.__gradeRepo.clear()
        grade1=Grade(6,7,0)      
        grade2=Grade(5,7,0)
        grade3=Grade(4,7,9)
        grade4=Grade(2,7,9)
        self.__gradeRepo.add(grade1)
        self.__gradeRepo.add(grade2)
        self.__gradeRepo.add(grade3)
        self.__gradeRepo.add(grade4)
        self.__gradeController.showUngraded(7)
    '''
    def __testStudentRemvoal(self):
        self.__gradeRepo.clear()
        self.__repository.clear()
        grade1=Grade(6,7,0)      
        grade2=Grade(5,7,0)
        grade3=Grade(4,7,9)
        grade4=Grade(2,7,9)
        student=Student(7,'Ion',100)
        self.__gradeRepo.add(grade1)
        self.__gradeRepo.add(grade2)
        self.__gradeRepo.add(grade3)
        self.__gradeRepo.add(grade4)
        self.__repository.add(student)
        #print(*self.__repository)
        #print(*self.__gradeRepo)
        self.__controller.removeStudent(7)
        self.__gradeController.removeStudent(7)
        #print(*self.__repository)
        #print(*self.__gradeRepo)
        assert self.__gradeRepo == []
        assert self.__repository == []
        
    def runTests(self):
        self.__testModel()
        self.__testValid()
        self.__testRepo()
        self.__testStudentController()
        self.__testGiveAssigStudent()
        self.__testGiveAssigGroup()
        self.__testGradeAssig()
        #self.__showUngraded()
        self.__testStudentRemvoal()
from Repository.Repository import Repository
from Errors import Errors
from Models.Entities import Student
class StudentCSVFileRepository(Repository):
    def __init__(self, fileName="students.txt"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, student):
        Repository.add(self, student)
        self.__storeToFile()
    
    def remove(self, student):
        Repository.remove(self, student)
        self.__storeToFile()        
    
    def clear(self):
        Repository.clear(self)
        self.__storeToFile()
    
    def update(self, student):
        Repository.update(self, student)
        self.__storeToFile()
    
    def __loadFromFile(self):
        try:
            f = open(self.__fName, "r")
            line = f.readline().strip()
            while line != "":
                attrs = line.split(";")
                student = Student(attrs[0], attrs[1], attrs[2])
                Repository.add(self, student)
                line = f.readline().strip()
        except IOError as e:
            raise e
        finally:
            f.close()
        
    def __storeToFile(self):
        f = open(self.__fName, "w")
        sts = Repository.getAll(self)
        for st in sts:
            strf = str(st.get_id()) + ";" + st.get_name() + ";" + str(st.get_group())
            strf = strf + "\n"
            f.write(strf)
        f.close()

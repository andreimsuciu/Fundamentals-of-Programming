from Repository.Repository import Repository
from Errors.Errors import RepositoryError
import pickle

class StudentPickleFileRepository(Repository):
    def __init__(self, fileName="students.pickle"):
        Repository.__init__(self)
        self.__fName = fileName
        self.__loadFromFile()
    
    def add(self, student):
        Repository.add(self, student)
        self.__storeToFile()
    
    def remove(self, student):
        Repository.remove(self,student)
        self.__storeToFile()        

    def clear(self):
        Repository.clear(self)
        self.__storeToFile()

    def update(self, student):
        Repository.update(self, student)
        self.__storeToFile()
          
    def __loadFromFile(self):
        f = open(self.__fName, "rb")
        
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def __storeToFile(self):
        f = open(self.__fName, "wb")
        pickle.dump(self._data, f)
        f.close()
        
        

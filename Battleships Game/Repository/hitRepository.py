from Errors.errors import RepositoryError
class HitRepo(object):
    '''
    This class holds the hits repo
    '''
    def __init__(self):
        self.__elems =[]
        for i in range(8):
            board_row = []
            for j in range(8):
                board_row.append('-')
            self.__elems.append(board_row)
    
    def __len__(self):
        return len(self.__elems)
    
    def __eq__(self, otherList):
        return self.__elems == otherList
    
    def __getitem__(self, position):
        return self.__elems[position]
    #def __getitem__(self, position1, position2):
    #    return self.__elems[position1][position2]    
   
    def update(self,x,y,value):
        for i in range(8):
            for j in range(8):
                if x==i and y==j:
                    self.__elems[i][j]=value
    
    def search(self,x,y):
        for i in range(8):
            for j in range(8):
                if x==i and y==j:
                    return self.__elems[i][j]
    
    def clear(self):
        for i in range(8):
            board_row = []
            for j in range(8):
                board_row.append('-')
            self.__elems.append(board_row)
    
    def getAll(self):
        return self.__elems[:]



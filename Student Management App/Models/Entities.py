class Student(object):

    def __init__(self, __id, __name, __group):
        self.__id = __id
        self.__name = __name
        self.__group = __group

    def __str__(self):
        return str(self.__id)+" "+self.__name+" "+str(self.__group)

    def __eq__(self, value):
        return self.__id == value.__id

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_name(self, value):
        self.__name = value

    def set_group(self, value):
        self.__val = value

    id = property(get_id, None, None, None)
    name = property(get_name, set_name, None, None)
    group = property(get_group, set_group, None, None)
    
class Assignment(object):
    
    def __init__(self, __id, __description, __deadline):
        self.__id = __id
        self.__description = __description
        self.__deadline = __deadline

    def __str__(self):
        return str(self.__id)+" "+self.__description+" "+str(self.__deadline)

    def __eq__(self, value):
        return self.__id == value.__id

    def get_id(self):
        return self.__id

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def set_description(self, value):
        self.__description = value

    def set_deadline(self, value):
        self.__deadline = value

    id = property(get_id, None, None, None)
    description = property(get_description, set_description, None, None)
    deadline = property(get_deadline, set_deadline, None, None)
    
class Grade(object):
    
    def __init__(self, __assignmentID, __studentID, __grade):
        self.__assignmentID = __assignmentID
        self.__studentID = __studentID
        self.__grade = __grade

    def __str__(self):
        return "Assignment:" + str(self.__assignmentID)+" "+"Student:"+str(self.__studentID)+" "+"Grade:"+str(self.__grade)

    def __eq__(self, value):
        return self.__assignmentID == value.__assignmentID and self.__studentID == value.__studentID

    def get_assignmentID(self):
        return self.__assignmentID

    def get_studentID(self):
        return self.__studentID

    def get_grade(self):
        return self.__grade

    def set_grade(self, value):
        self.__grade = value

    assignmentID = property(get_assignmentID, None, None, None)
    studentID = property(get_studentID, None, None, None)
    grade = property(get_grade, set_grade, None, None)



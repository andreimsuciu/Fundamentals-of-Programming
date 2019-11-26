from Errors.Errors import RepositoryError, ValidError, GradingError

class Console(object):
    
    
    def __init__(self, __studentCtrl,__assigCtrl,__gradeCtrl):
        self.__studentCtrl =__studentCtrl
        self.__assigCtrl = __assigCtrl
        self.__gradeCtrl =__gradeCtrl
    
    def printMenu(self):
        print ("help")
        print ("exit\n")  
        print ("Possible commands for student:")
        print ("1.add student <studentID>, <name>, <group>")
        print ("2.remove student <studentID>")
        print ("3.update student <studentID>, <name>, <group>")
        print ("4.list students\n")
        print ("Possible commands for assignments:")
        print ("1.add assig <assignmentID>,  <description>, <deadline>")
        print ("2.remove assig <assignmentID>")
        print ("3.update assig <assignmentID>,  <description>, <deadline>")
        print ("4.list assigs\n")
        print ("Possible commands for giving and grading assignments:")
        print ("1.give group <group> <assignment ID>")
        print ("2.give student <student> <assignment ID>")
        print ("NB! Assignments can be given only once!")
        print ("3.ungraded <studentID>")   
        print ("4.grade <assigID> , <studentID>, <grade>\n")    
    
    def __uiUngraded(self,params):
        if len(params)!=1:
            print("invalid no of params!")
            return
        studentID=params[1]
        for i in self.__gradeCtrl.__gradeRepo:
            if studentID==self.__gradeCtrl.Grade.get_studentID(i):
                if self.__gradeCtrl.Grade.get_grade(i) == 0:
                    print (str(i))
                    
    def __uiGive(self,params):
        cmd = params[0]
        if cmd == "student":
            self.__uiGiveStudent(params[1:])
        elif cmd == "assig":
            self.__uiGiveGroup(params[1:])
        else:
            print("invalid command!")
            return
        
    def __uiGiveStudent(self,params):
        if len(params)!=2:
            print("invalid no of params!")
            return
        studentid=int(params[0])
        assigid=int(params[1])
        self.__gradeCtrl.giveAssigStudent(assigid,studentid)
        
    def __uiGiveGroup(self,params):
        if len(params)!=2:
            print("invalid no of params!")
            return
        group=int(params[0])
        assigid=int(params[1])
        self.__gradeCtrl.giveAssigStudent(assigid,group)
            
    def __uiAdd(self,params):
        cmd = params[0]
        if cmd == "student":
            self.__uiAddStudent(params[1:])
        elif cmd == "assig":
            self.__uiAddAssig(params[1:])
        else:
            print("invalid command!")
            return
        
    def __uiAddStudent(self,params):
        if len(params)!= 3:
            print("invalid no of params!")
            return 
        ident = int(params[0])
        name = params[1]
        group = int(params[2])
        self.__studentCtrl.addStudent(ident,name,group)
    
    def __uiAddAssig(self,params):
        if len(params)!= 3:
            print("invalid no of params!")
            return 
        ident = int(params[0])
        desc = params[1]
        deadline = int(params[2])
        self.__assigCtrl.addAssignment(ident,desc,deadline) 
           
    def __uiRemove(self,params):
        cmd = params[0]
        if cmd == "student":
            self.__uiRemoveStudent(params[1:])
        elif cmd == "assig":
            self.__uiRemoveAssig(params[1:])
        else:
            print("invalid command!")
            return

    def __uiRemoveStudent(self,params):
        if len(params)!=1:
            print("Invalid no of params!")
            return
        ident=int(params[0])
        self.__studentCtrl.removeStudent(ident)
        self.__gradeCtrl.removeStudent(ident)
    
    def __uiRemoveAssig(self,params):
        if len(params)!=1:
            print("Invalid no of params!")
            return
        ident=int(params[0])
        self.__assigCtrl.removeAssignment(ident)
        self.__gradeCtrl.removeAssig(ident)    
        
    def __uiUpdate(self,params):
        cmd = params[0]
        if cmd == "student":
            self.__uiUpdateStudent(params[1:])
        elif cmd == "assig":
            self.__uiUpdateAssig(params[1:])
        else:
            print("invalid command!")
            return
        
    def __uiUpdateStudent(self,params):
        if len(params)!= 3:
            print("invalid no of params!")
            return 
        ident = int(params[0])
        name = params[1]
        group = int(params[2])
        self.__studentCtrl.updateStudent(ident,name,group)
        
    def __uiUpdateAssig(self,params):
        if len(params)!= 3:
            print("invalid no of params!")
            return 
        ident = int(params[0])
        desc = params[1]
        deadline = int(params[2])
        self.__assigCtrl.updateAssignment(ident,desc,deadline)
            
    def __uiList(self,params):
        try:
            cmd = params[0]
            if cmd == "student":
                self.__uiListStudent(params[1:])
            elif cmd == "assig":
                self.__uiListAssig(params[1:])
        except IndexError:
            print("what to list was not specified!")
            return            
    
    def __uiListStudent(self,params):
        if len(params)!=0:
            print("invalid no of params!")
            return
        students=self.__studentCtrl.getAllStudents()
        if len(students)==0:
            print("No students in database!")
            return
        s =""
        for x in students:
            s+=str(x)+"\n"
        print(s)
        
    def __uiListAssig(self,params):
        if len(params)!=0:
            print("invalid no of params!")
            return
        assigs=self.__assigCtrl.getAllAssigs()
        if len(assigs)==0:
            print("No assignments in database!")
            return
        s =""
        for x in assigs:
            s+=str(x)+"\n"
        print(s)
        
    def run(self):
        self.printMenu()
        commands={"add":self.__uiAdd,"remove":self.__uiRemove,"update":self.__uiUpdate,"list":self.__uiList,"give":self.__uiGive,"ungraded":self.__uiUngraded}
        while True:
            cmd = input(">>")
            params = cmd.split()
            if cmd == "exit":
                return
            elif cmd == "help":
                self.printMenu()
            elif params[0] in commands:
                try:
                    commands[params[0]](params[1:])
                except ValueError:
                    print("invalid numeric value given!")
                except RepositoryError as re:
                    print("Repository Error:")
                    print(re)
                except ValidError as ve:
                    print("Validation Error:")
                    print(ve)
                except GradingError as g:
                    print("Grading Error:")
                    print(g)
            else:
                print("invalid command!")
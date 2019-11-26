from Errors.Errors import ValidError

class studentValidator(object):
    def validateStudent(self,student):
        errors = ""
        if student.get_id()<0:
            errors+="id is invalid!\n"
        if student.get_name()=="":
            errors+="name cannot be empty!\n"
        if student.get_group()<0 or student.get_group()>999:
            errors+="group is invalid!\n"
        if len(errors)>0:
            raise ValidError(errors)
        
class assigValidator(object):
    def validateAssig(self,assig):
        errors = ""
        if assig.get_id()<0:
            errors+="id is invalid!\n"
        if assig.get_description()=="":
            errors+="description cannot be empty!\n"
        if assig.get_deadline() < 0 or assig.get_deadline() > 31:
            errors+="deadline is invalid!\n"
        if len(errors)>0:
            raise ValidError(errors)
    
class gradeValidator(object):
    def validateIDs(self,grade):
        errors = ""
        if grade.get_assignmentID()<0:
            errors+="assignmentID is invalid\n"
        if grade.get_studentID()<0:
            errors+="studentID is invalid\n"
        if len(errors)>0:
            raise ValidError(errors)
    def validateGrade(self,grade):
        errors = ""
        if grade.get_grade()<0 or grade.get_grade()>10:
            errors+="Grade is invalid!\n"    
        if len(errors)>0:
            raise ValidError(errors)
            
    def vallidateID(self,assigID,gradeList):
        '''
        this function checks wether the given assignment id is already in the gradeList
        in:grade-object
            gradeList-list of grades
        out:raises ValidError if the id is already in the list
        '''
        if gradeList == []:
            return
        else:
            for i in gradeList:
                if assigID==i.get_assignmentID():
                    raise ValidError("Assignment already given!")
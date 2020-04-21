class Student:
    def __init__(self,string):
        self.string = string
        if string is "":
            return
        self.LN = string.split(" '")[1]

        self.FN = string.split (" '")[2]

        self.MN = string.split(" '")[3].strip(")")

        self.PN = string.split(" '")[4]

        self.EM = string.split(" '")[5].split(" ")[0]

        self.GPA = string.split(" '")[5].split(" ")[1].strip(" )")

class info:
    def __init__(self):
        self.student = []
        f = open("Students.txt",'r')
        for line in f:
                if "(LIST (LIST " in line:
                    obj = Student(line)
                    self.student.append(obj)
        f.close()

    def gpaMoreThan3 (info):
        counter = 0
        for line in info.student:
            if float (line.GPA) >= 3:
                counter += 1
        print counter

    def eMail (info):
        counter = 0
        for line in info.student:
            if line.EM == "NONE":
                counter += 1
        print counter 

    def avgGPA (info):
        Total = 0
        for line in info.student:
            Total += float(line.GPA)
        avg = Total/len(info.student)
        print avg

    def Save(info):
        f = open("Students.txt", 'w')

        f.write("students (LIST\n")
        
        for item in info.student:
            f.write("(LIST (LIST '"+item.LN + " '"+item.FN +" '"+item.MN +" '"+item.PN +" '"+item.EM +" '" + item.GPA + " )")
            f.write("\n")
        f.write(" ) )")
        f.close()
        Save = 1

                
            

    def addStudent(self):        
        objStudent = Student("")
        objStudent.LN = raw_input("Enter the student's last name")
        objStudent.FN = raw_input("Enter the student's first name")
        objStudent.MN = raw_input("Enter the student's middle name")
        objStudent.PN = raw_input("Enter the student's phone number")
        objStudent.EM = raw_input("Enter the student's email address")
        objStudent.GPA = raw_input("Enter the student's GPA")
        self.student.append(objStudent)

informationObj = info()

informationObj.gpaMoreThan3()

informationObj.eMail()

informationObj.avgGPA()

informationObj.addStudent()




for item in informationObj.student:
    if item.FN == "Malachi" and item.LN == "Constant":
        break
else:
    studentObj = Student("(LIST (LIST 'Constant 'Malachi 'M ) 'NONE 'bmabbott@mail.usi.edu 3.1915725161177115")
    informationObj.student.append(studentObj)

informationObj.Save()   

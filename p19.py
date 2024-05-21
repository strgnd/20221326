class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
class GraduateStudent(Student):
    def __init__(self, name = 'Jeong Hyeonji', age = 22, graduateID = 2022, major = 'Internet of Things'):
        super().__init__(name, age)
        self.graduateID = graduateID
        self.major = major

    def getID(self):
        return self.graduateID
    def getMajor(self):
        return self.major
    
    def printmy(self):
        print("graduateID, major", self.graduateID)
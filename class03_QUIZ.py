class Student():
    def __init__(self,korean,english,math):
        self.korean = korean
        self.english = english
        self.math = math
    
    def showKorean(self):
        print(self.korean)
    def showEnglish(self):
        print(self.english)
    def showMath(self):
        print(self.math)
    def showAverage(self):
        total_score = self.korean + self.english + self.math
        print(total_score/3)


lee = Student(100,99,98)
lee.showKorean()
lee.showEnglish()
lee.showMath()
lee.showAverage()


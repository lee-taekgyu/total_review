d_persons = {'Guillaume':'Canada', 'Niklas':'Germany', 'Mark':'USA', 'Alex':'Swiss', 'Alberto':'Italia'}

class Person():
    nation = "A nation"
    name = "username"

    def setNation(self, target):
        self.name = target
    def showNation(self):
        print(d_persons[self.name])

p1 = Person()
p1.setNation('Guillaume')
p1.showNation()


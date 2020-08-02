d_persons = {'Guillaume':'Canada', 'Niklas':'Germany', 'Mark':'USA', 'Alex':'Swiss', 'Alberto':'Italia'}
class Person():
    nation = 'A nation'
    name = 'username'
    def setName(self, target):
        self.name = target
    def findNation(self,d_dict):
        self.nation = d_dict[self.name]
    def showName(self):
        print(self.name,end=' ')
    def showNation(self):
        print(self.nation, end=' ')



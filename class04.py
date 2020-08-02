class Cat():
    def snack(self):
        print('myeo~')

class Koshort(Cat):
    def setAge(self,Age):
        self.__age = Age
        print("sef age to {}.".format(Age))
    def showAge(self):
        print("{} years old.".format(self.__age))
    def snack(self):
        print("YAYA")

minyong = Koshort()
minyong.setAge(7)
minyong.snack()
minyong.showAge()

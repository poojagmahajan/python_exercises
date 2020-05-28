

class student :
    def __init__(self,name,phy,chem,bio):
        self.name = name
        self.phy = phy
        self.chem= chem
        self.bio = bio

    def totalObtained(self):
        print('student name :',self.name)
        total= self.phy + self.chem + self.bio
        print('total marks :',total)
        return total

    def percentage(self):
        percetage = (self.totalObtained()/300)*100
        return percetage

obj1 = student('pooja',70,80,90)
print(obj1.percentage())

obj2 = student('gaurav',90,80,90)
print(obj2.percentage())
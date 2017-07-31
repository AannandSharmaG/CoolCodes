class HomoSapiens():
    species = 'Homosapiens'

class Male():
    gender = 'Male'

class Student(Male,HomoSapiens):
    def intro(self):
        print('Species = ' + HomoSapiens.species)
        print('Gender = ' + Male.gender)


s = Student()
s.intro()


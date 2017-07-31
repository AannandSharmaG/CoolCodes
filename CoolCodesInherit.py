class HomoSapiens():
    def purposeOfLife(self):
        print('To find the wisdom')

class Male(HomoSapiens):
    gender = 'Male'
    def introduceYourself(self,rel):
        self.relation = rel
        print('I am a '+self.gender+" And your "+self.relation)

class Female(HomoSapiens):
    gender = 'female'
    def introduceYourself(self,rel):
        self.relation = rel
        print('I am a '+self.gender+" And your "+self.relation)
    def purposeOfLife(self):
        print('To bestow love upon others')


Sally= Female()
Sally.introduceYourself('girlfriend')
Sally.purposeOfLife()

Arun = Male()
Arun.introduceYourself('Father')
Arun.purposeOfLife()




class GirlFriend:
    def __init__(self,name,rating):
        self.name = name
        self.hotQuo = rating
    def howMuchHot(self):
        print("You rated "+self.name +" "+ str(self.hotQuo) + " on hot quotient scale.")

g1 = GirlFriend('Sally',5)
g1.howMuchHot()

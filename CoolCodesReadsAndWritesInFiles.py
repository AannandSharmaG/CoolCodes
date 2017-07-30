fw = open("myStory.txt",'w')
fw.write('Hi I am Aannand Sharma.\n')
fw.write('I am cool and my codes are even cooler...')
fw.close()

fr = open('myStory.txt','r')
ALegendsStory = fr.read()
print(ALegendsStory)
fr.close()
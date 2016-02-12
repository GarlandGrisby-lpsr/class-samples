def choice1():
        print "Whats your files name?"
        fileName = str(raw_input())
        MyFile = open('pumas.tmd', 'r')
        print(MyFile.read())
def choice1T():
        pass
def answer():
        pass
def answer2():
        pass
def answer3():
        pass
print ''' Would you like to... 
 (1) Open An Old File
or 
 (2) Create a new team?'''
userChoice = int(raw_input())
if userChoice == 1:
       choice1()


 


 

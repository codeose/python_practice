class ListnTuple(): #creating a class
    def listGarner(self):   #defining the first method in the class
        num = (input('Enter some numbers seperated by a comma: '))  #taking input from the console and storing in 'num' variable
        return num
    def listAndTupleGenertor(self):     #defining the second method
        num = self.listGarner()
        list = num.split(',')         #generating a list from the num variable
        t = tuple(list)    #generating a tuple from the list
        print("Generated List:", list) #printing out the list on the console
        print("Generated Tuple:", t)   #printing out the tuple on the console


gen1 = ListnTuple() #creating an object for the class
gen1.listAndTupleGenertor() #calling the method using the object
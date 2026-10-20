class Get: 
    def first(self): 
        print("This is the first method of the Get class.") 

class Set: 
    def second(self): 
        print("This is the second method of the Set class.") 

class Delete(Get, Set): 
    def third(self): 
        print("This is the third method of the Delete class.") 

# Creating the instance using PascalCase for the class name
delete_instance = Delete() 

delete_instance.first() 
delete_instance.second() 
delete_instance.third()

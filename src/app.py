
class Employee: # create Employee class name  
    dept = 'Information technology'  # define class variable  
    def __init__(self, name, id):  
        self.name = name       # instance variable  
        self.id = id             # instance variable  

def main():
    e1 = Employee('E1', 1)
    e2 = Employee('E2', 2)
    Employee.dept = 'test'
    print(e2.dept)

if __name__ == '__main__':
    main()


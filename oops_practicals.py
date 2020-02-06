class Employee:
    raise_amount = 1.04
    no_of_emp = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        #this is a case  where we use the class to set the variable not the instance
        Employee.no_of_emp +=1
    
    def introduce_self(self):
        print('My name is %s %s' %(self.first, self.last))
    #using a class variable in method
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount )
        return self.pay
print(Employee.no_of_emp)

emp1 = Employee('Damian', 'Marley', 5000)
emp2 = Employee('Judith', 'Aleke', 6000)

#using the instance to run the method
emp1.introduce_self()

#using the class to run the introduce_self method and passing the istance as an argument
Employee.introduce_self(emp2)

print(emp1.apply_raise())
print(emp2.apply_raise())
        
print(Employee.no_of_emp)

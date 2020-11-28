class Person:
    
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if self.age <0:
            self.age = 0
            print('Age is not valid, setting age to 0')
    
    def amIOld(self):
        if self.age < 13:
            print('You are young')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager')
        else:
            print('You are old')
            
    def yearPasses(self):
        self.age +=1

x = Person(-1)
x.yearPasses()
x.amIOld()
y = Person(10)
y.yearPasses()
y.amIOld()
z = Person(16)
z.yearPasses()
z.amIOld()

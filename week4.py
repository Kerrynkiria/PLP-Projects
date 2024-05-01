class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def introduce(self):
        print(f"My name is {self.name},I'm a {self.gender} and of {self.age} years.")
        
        
new=Person("Kerry Nkiria", 18, "Male")
new.introduce()

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nOccupation: {self.occupation}")



rohit = Person("rohit", 26, "Software Engineer")
rohit.info()

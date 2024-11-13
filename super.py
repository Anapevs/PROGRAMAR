class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet (self):
        print ("hello, ima a person")
#super se usa para llamar a los atributos en el constructo de la clase heredada 
class Student (Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print (f"Hello, your ID is {self.student_id}.")

student = Student ("Ana", 20, "s16")
student.greet()
#Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)
#Crear un constructor que inicialice los atributos
#Crear un método llamado add_grade que recibe un número como parámetro y lo agrega a la lista grades.
#Crear otro método llamado average_grade que calcule y retorne la nota promedio de la lista de notas grades


class Student:
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

student1 = Student("Juan", 20)
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)
average = student1.average_grade()
print(f"El promedio de notas de {student1.name} es: {average}")
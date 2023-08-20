#Crear una lista de diccionarios donde cada diccionario contiene la información de un estudiante.
#Usar un list comprehension para crear una lista de objetos de la clase Student a partir de la lista de diccionarios.
#Usar otro list comprehension para filtrar los estudiantes, excluyendo los que tienen una nota promedio menor que un umbral dado.
#Usar un dictionary comprehension para crear un diccionario de estudiantes que tienen una nota promeidio por encima de un umbral dado, con los nombre de los estudiantes como claves y el objeto Student como valor.

class Student:
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0  # Retorna 0 si no hay notas en la lista
        return sum(self.grades) / len(self.grades)


student_data = [
    {"name": "Juan", "age": 20, "grades": [85, 90, 78]},
    {"name": "María", "age": 22, "grades": [92, 88, 95]},
    {"name": "Carlos", "age": 21, "grades": [75, 80, 70]}
]
students = [Student(data["name"], data["age"], data["grades"]) for data in student_data]

umbral = 80

passing_students = [student for student in students if student.average_grade() >= umbral]

passing_students_dict = {student.name: student for student in passing_students}

print("Diccionario de estudiantes aprobados:")
for name, student in passing_students_dict.items():
    print(f"Nombre: {name}, Edad: {student.age}, Promedio de notas: {student.average_grade()}")
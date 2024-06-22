# Create class Student, Doctor, Teacher with method print infor of object
class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade
    def describe(self):
        return (f'Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}')

class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject
    def describe(self):
        return (f'Teacher - Name: {self.name} - YoB: {self.yob} - Grade: {self.subject}')

class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist
    def describe(self):
        return (f'Doctor - Name: {self.name} - YoB: {self.yob} - Grade: {self.specialist}')

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        description = f"Ward: {self.name}\n"
        for person in self.people:
            description += person.describe() + "\n"
        return description

    # Count Doctor
    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    # Sort age
    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    # Compute the average YoB
    def compute_average_yob(self):
        total_yob = 0
        for person in self.people:
            total_yob += person.yob
        return total_yob / len(self.people)
# Examples
# 2(a)
student1 = Student(name =" studentA ", yob =2010 , grade ="7")
student1.describe()

teacher1 = Teacher(name =" teacherA ", yob =1969 , subject =" Math ")
teacher1.describe()

doctor1 = Doctor(name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
doctor1.describe()

# 2(b) add people into Ward

teacher2 = Teacher(name =" teacherB ", yob =1995 , subject =" History ")
doctor2 = Doctor(name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward1 = Ward(name =" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.describe())

# 2(c) count Doctor in Ward
print(f"\nNumber of doctors : {ward1.count_doctor()}")

# 2(d) sort people in Ward by age
print ("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
print(ward1.describe())

# 2(e) compute average yob
print(f"\nAverage year of birth ( teachers ): {ward1.compute_average_yob()}")
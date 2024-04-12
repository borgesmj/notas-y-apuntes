# Creamos un contructor general
class job:
  type_of_job = None
  salary = None
  hours = None

  def __init__(self, type_of_job, salary, hours):
    self.type_of_job = type_of_job
    self.salary = salary
    self.hours = hours

# imprimimos la clase padre
  def print(self):
    print("== JOB ==")
    print(f"""
    Type of Job: {self.type_of_job}
    Salary: {self.salary}
    Hours: {self.hours}
    """)

# creamos la clase hija doctor que tiene job como parametro
class doctor(job):
#le agregamos dos nuevos parametros
  experience = None
  speciality = None

  def __init__(self, salary, hours, experience, speciality):
    self.type_of_job = 'Doctor'
    self.salary = salary
    self.hours = hours
    self.experience = experience
    self.speciality = speciality
  def print(self):
    print("== JOB ==")
    print(f"""
    Type of Job: {self.type_of_job}
    Salary: {self.salary}
    Hours: {self.hours}
    Years = {self.experience}
    Speciality = {self.speciality}
    """)

# creamos la clase hija techaer que tiene job como parametro
class teacher(job):
#le agregamos dos nuevos parametros
  subject = None
  position = None

  def __init__(self, salary, hours, subject, position):
    self.type_of_job = 'Teacher'
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position
  def print(self):
    print("== JOB ==")
    print(f"""
    Type of Job: {self.type_of_job}
    Salary: {self.salary}
    Hours: {self.hours}
    Subject = {self.subject}
    Position = {self.position}
    """)



lawyer = job("Lawyer", "$100,000", "40")
doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
teacher = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
lawyer.print()
doc.print()
teacher.print()
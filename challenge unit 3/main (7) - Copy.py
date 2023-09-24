def __init__(self, name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
     self.cgpa
def sort_student(student_list):
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,teverse=true)
return sorted_students
students=[
student("stephen","A123",7.8),student("karthik","A124",8.9),student("santhosh","A125",9.1),student("komban","A126"9.9)]
sorted_students = sort_student(students)
for student in sorted_students:
   print("name: {}, roll number: {} , cgpa: {}".format(student.name,student.roll_number, student.cgpa))

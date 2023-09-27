def__init__(self,name,roll_number,cgpa):
self.name = Name
self.roll_number =roll_number
self.cgpa = cgpa
def sort_students = sorted(students_list):
sorted.students = sorted(student_list,
                         key=lambda student: student.cgpa,
                         reverse=True)
return sorted_students
students = [
  student("ajee" , "a123" , 7.8)
  student("zulfa" , "a124" , 9.8)
  student("harini" , "a125" , 8.8) 
  student("mupss" , "a126" , 6.8)
]
sorted_students = sort_students(students)
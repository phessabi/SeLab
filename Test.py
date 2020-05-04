from Models.Student import Student
from Models.Professor import Professor
from Models.Course import Course


ml = Course(40441, 'Machine Learning', 'ce')
deep = Course(40123, 'Deep Learning', 'ce')
parham = Student(94109562, 'Parham Hessabi', 'ce')
soleimani = Professor(4112412, 'Mahdie Soleimani', 123, 132)
soleimani.present_course(ml)
soleimani.present_course(deep)

parham.enroll(ml, soleimani)
parham.enroll(deep, soleimani)
parham.finish("Machine Learning", 9)
parham.finish("Deep Learning", 15)

print(parham.grade("Machine Learning"))
print(parham.grade("Deep Learning"))
print(soleimani.salary)
print(parham.average)

#we take in how many courses the student has and store it in a variable to be able to iterate using that
#variable
courses = int(input("Enter the number of courses: "))
#we set a variable "total_marks" to 0, we use this variable to calculate the total marks of student
total_marks = 0
for i in range(courses):
    marks = int(input("Enter your course marks: "))
    total_marks = total_marks + marks

#dividing the total marks by the number of courses will give us the average
avg = total_marks/courses
print("Your average for all courses is ", avg)
#assuming that the total possible mark to get is 500 we set a variable with the value 500 and we divide
#the total marks by that variable and multiply by 100 to get a percentage
assumed_total_mark = 500
percentage = (total_marks/assumed_total_mark) * 100
print("Your percentage is " , percentage, "%")

    
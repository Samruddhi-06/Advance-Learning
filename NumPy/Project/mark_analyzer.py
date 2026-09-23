# Project: Student Marks Analyzer

# Build a program that analyzes marks of students in multiple subjects using only NumPy.

# What your project should calculate

# Basic information -> Number of students, Number of subjects, Shape of the dataset
# What your project should calculate -> Basic information, Number of students, Number of subjects, Shape of the dataset
# Student-wise analysis -> Total marks of every student, Average marks of every student, Highest mark, Lowest mark, Students scoring above a particular average
# Subject-wise analysis -> Average marks in each subject, Highest mark in each subject, Lowest mark in each subject, Subject with the highest average
# Performance analysis -> Overall class average, Highest-performing student, Lowest-performing student, Number of students who passed, Number of students who failed

import numpy as np

marks = np.array([
    [78, 85, 92, 67, 88],
    [56, 72, 68, 75, 61],
    [91, 89, 95, 94, 90],
    [45, 55, 48, 52, 60],
    [82, 79, 85, 88, 91]
])

students = np.array(['1','2','3','4','5'])

# rows -> students & cols -> subjects

#  Number of students
no_of_stud = np.size(marks,axis=0)
print("Total students =",no_of_stud)

# Number of subjects
no_of_subjects = np.size(marks,axis=1)
print("Total subjects =",no_of_subjects)

# Shape of the dataset
shape = np.shape(marks)
print("Shape of dataset =",shape)

print()
print("-------------------------------------------------")

# Total marks of every student
a1 = marks[0]
s1 = np.sum(a1)
print("Total marks of student1 =",s1)
a2 = marks[1]
s2 = np.sum(a2)
print("Total marks of student2 =",s2)
a3 = marks[2]
s3 = np.sum(a3)
print("Total marks of student3 =",s3)
a4 = marks[3]
s4 = np.sum(a4)
print("Total marks of student4 =",s4)
a5 = marks[4]
s5 = np.sum(a5)
print("Total marks of student5 =",s5)

total_marks = [s1,s2,s3,s4,s5]

print()
print("-------------------------------------------------")

# Average marks of every student
avg1 = np.mean(a1)
avg2 = np.mean(a2)
avg3 = np.mean(a3)
avg4 = np.mean(a4)
avg5 = np.mean(a5)
print("Average marks of student1 =",avg1)
print("Average marks of student2 =",avg2)
print("Average marks of student3 =",avg3)
print("Average marks of student4 =",avg4)
print("Average marks of student5 =",avg5)

total_avg = [avg1,avg2,avg3,avg4,avg5]

print()
print("-------------------------------------------------")

# Highest total mark by a student
highest_marks = np.max(total_marks)
print("Highest marks =",highest_marks)

# Lowest total marks by a student
lowest_marks = np.min(total_marks)
print("Lowest marks =",lowest_marks)

print()
print("-------------------------------------------------")

# Students scoring above a particular average
threshold = 75.0
avg_marks = np.array(total_avg)
above_avg = students[avg_marks > threshold]
print("Students scoring above average marks =",above_avg)

print()
print("-------------------------------------------------")

# Average marks in each subject
b1 = marks[:,0]
sub1_avg = np.mean(b1)
print("Average marks of subject 1 =",sub1_avg)
b2 = marks[:,1]
sub2_avg = np.mean(b2)
print("Average marks of subject 2 =",sub2_avg)
b3 = marks[:,2]
sub3_avg = np.mean(b3)
print("Average marks of subject 3 =",sub3_avg)
b4 = marks[:,3]
sub4_avg = np.mean(b4)
print("Average marks of subject 4 =",sub4_avg)
b5 = marks[:,4]
sub5_avg = np.mean(b5)
print("Average marks of subject 5 =",sub5_avg)

sub_avg = np.array([sub1_avg,sub2_avg,sub3_avg,sub4_avg,sub5_avg])

print()
print("-------------------------------------------------")

# Highest mark in each subject

print("Highest marks in subject 1 =",np.max(b1))
print("Highest marks in subject 2 =",np.max(b2))
print("Highest marks in subject 3 =",np.max(b3))
print("Highest marks in subject 4 =",np.max(b4))
print("Highest marks in subject 5 =",np.max(b5))

print()
print("-------------------------------------------------")

# Lowest mark in each subject

print("Lowest marks in subject 1 =", np.min(b1))
print("Lowest marks in subject 2 =", np.min(b2))
print("Lowest marks in subject 3 =", np.min(b3))
print("Lowest marks in subject 4 =", np.min(b4))
print("Lowest marks in subject 5 =", np.min(b5))

print()
print("-------------------------------------------------")

# Subject with the highest average

print(f"Highest average among 5 subject is {np.max(sub_avg)} of student {np.argmax(sub_avg)+1} subject")

print()
print("-------------------------------------------------")

# Overall class average

print("Overall class average =", np.mean(marks))

print()
print("-------------------------------------------------")

# Highest-performing student

print(f"Highest performing student is student {np.argmax(total_marks)+1} with total marks {np.max(total_marks)}")

# Lowest-performing student

print(f"Lowest performing student is student {np.argmin(total_marks)+1} with total marks {np.min(total_marks)}")

print()
print("-------------------------------------------------")

# Number of students who passed

passing = 75

passed = students[avg_marks >= passing]
print("Students passed =",passed)
print("Number of students passed =",np.size(passed))

# Number of students who failed

failed = students[avg_marks < passing]
print("Students failed =",failed)
print("Number of students failed =",np.size(failed))


print()
print("-------------------------------------------------")
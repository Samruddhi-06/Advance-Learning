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

# Highest mark
highest_marks = np.max(total_marks)
print("Highest marks =",highest_marks)

# Lowest marks
lowest_marks = np.min(total_marks)
print("Lowest marks =",lowest_marks)

# Students scoring above a particular average
threshold = 75.0
avg_marks = np.array(total_avg)
above_avg = students[avg_marks > threshold]
print("Students scoring above average marks =",above_avg)

# Average marks in each subject
b1 = marks[:,0]
sub1_avg = np.mean(b1)
print("Average marks of subject 1 =",sub1_avg)
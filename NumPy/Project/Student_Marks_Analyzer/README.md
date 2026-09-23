# 📊 Student Marks Analyzer

A beginner-friendly **NumPy project** that analyzes student marks across multiple subjects. This project was built to practice NumPy arrays, indexing, slicing, aggregation, Boolean indexing, and other fundamental NumPy concepts through a practical problem.

## 🎯 Project Objective

The goal of this project is to analyze student performance using **only NumPy** and calculate useful student-wise, subject-wise, and overall performance statistics.

## 🛠️ Technologies Used

* **Python**
* **NumPy**

## 📌 Dataset

The project uses a 2D NumPy array where:

* Each **row** represents a student.
* Each **column** represents a subject.
* Each value represents the marks obtained by a student in a subject.

Example:

```python
marks = np.array([
    [78, 85, 92, 67, 88],
    [56, 72, 68, 75, 61],
    [91, 89, 95, 94, 90],
    [45, 55, 48, 52, 60],
    [82, 79, 85, 88, 91]
])
```

## 📋 Features

### 1. Basic Information

The program calculates:

* Number of students
* Number of subjects
* Shape of the dataset

### 2. Student-wise Analysis

For every student, the program calculates:

* Total marks
* Average marks

It also identifies:

* Highest total marks
* Lowest total marks
* Students scoring above a specified average

### 3. Subject-wise Analysis

For every subject, the program calculates:

* Average marks
* Highest marks
* Lowest marks

It also identifies:

* Subject with the highest average

### 4. Performance Analysis

The program calculates:

* Overall class average
* Highest-performing student
* Lowest-performing student
* Students who passed
* Students who failed
* Number of students who passed
* Number of students who failed

The current passing criterion is:

```text
Average marks >= 75
```

## 🧠 NumPy Concepts Practiced

This project helped me practice the following NumPy concepts:

* `np.array()`
* `np.size()`
* `np.shape()`
* Array indexing
* Array slicing
* Row and column selection
* Boolean indexing
* `np.sum()`
* `np.mean()`
* `np.max()`
* `np.min()`
* `np.argmax()`
* `np.argmin()`
* Working with `axis`
* 2D arrays
* Basic statistical analysis

## 🔎 Example of Boolean Indexing

Students scoring above the specified threshold are selected using a Boolean condition:

```python
above_avg = students[avg_marks > threshold]
```

This creates a Boolean mask and uses it to select the corresponding students.

## 📚 Key Learning

One of the main concepts practiced through this project is the use of **axes** in NumPy.

For a 2D marks array:

```python
np.sum(marks, axis=1)
```

calculates the total marks for each student.

While:

```python
np.mean(marks, axis=0)
```

calculates the average marks for each subject.

This helped me understand how NumPy performs calculations across rows and columns.

## 🚀 Future Improvements

Possible improvements for future versions:

* Use `axis` to reduce repetitive calculations
* Add student names instead of only student numbers
* Add subject names
* Add pass/fail criteria for individual subjects
* Calculate standard deviation
* Sort students according to performance
* Add ranking
* Handle missing values using `NaN`
* Create a more interactive version

## 📁 Project Structure

```text
Advance Learning /
|
Project /
|
Student_Marks_Analyzer/
│
├── student_marks_analyzer.py
└── README.md
```

## ✅ Conclusion

This project provided practical experience with NumPy and demonstrated how numerical arrays can be used to perform student performance analysis efficiently.

It also strengthened my understanding of **indexing, slicing, Boolean indexing, aggregation, `argmax()`, `argmin()`, and axes**, which are important concepts for further learning in data analysis.

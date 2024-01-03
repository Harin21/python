#create class stud with members roll no. name course and total mark write constructor and methods to add 10 marks to all stud with total mark>400
class Student:
    def __init__(self, roll_no, name, course, total_marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.total_marks = total_marks

    def add_10_marks(self):
        if self.total_marks > 400:
            self.total_marks += 10

    def display_info(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Course: {self.course}, Total Marks: {self.total_marks}"


# Example usage:
# Creating instances of the Student class
student1 = Student(101, "John Doe", "Computer Science", 420)
student2 = Student(102, "Jane Smith", "Mathematics", 380)

# Displaying information before adding 10 marks
print("Before adding 10 marks:")
print(student1.display_info())
print(student2.display_info())

# Adding 10 marks to students with total marks > 400
student1.add_10_marks()
student2.add_10_marks()

# Displaying information after adding 10 marks
print("\nAfter adding 10 marks:")
print(student1.display_info())
print(student2.display_info())


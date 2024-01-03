# write a prgrm to create a file with names of 10 stud read the file and store it into a list
# Write names to a file
with open("stud.txt", "w") as file:
    for i in range(1, 11):
        name = input(f"Enter the name of student {i}: ")
        file.write(name + "\n")

# Read names from the file and store them in a list
student_names = []
with open("stud.txt", "r") as file:
    for line in file:
        student_names.append(line.strip())

# Display the list of student names
print("List of student names:")
print(student_names)


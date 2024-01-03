#create a csv file with name roll and course read  specific columns of the csv file and print the contents of the columns 
import csv

# Create a CSV file with name, roll, and course columns
with open("student_data.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Roll", "Course"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Write sample data
    writer.writerow({"Name": "John Doe", "Roll": 101, "Course": "Computer Science"})
    writer.writerow({"Name": "Jane Smith", "Roll": 102, "Course": "Mathematics"})
    writer.writerow({"Name": "Bob Johnson", "Roll": 103, "Course": "Physics"})

# Read specific columns from the CSV file and print the contents
columns_to_read = ["Name", "Course"]

with open("student_data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Print headers of the selected columns
    print("\t".join(columns_to_read))

    # Print data from selected columns
    for row in reader:
        row_data = "\t".join([row[column] for column in columns_to_read])
        print(row_data)


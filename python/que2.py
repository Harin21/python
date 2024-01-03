#create a list of nos. perform the following ops. ,smallest no. from the list,largest no. from the list,remove duplicate from the list,append a list of the numbers to the existing list

l1= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
smallest_number = min(l1)
largest_number = max(l1)
print(f"Original List: {l1}")
print(f"Smallest Number: {smallest_number}")
print(f"Largest Number: {largest_number}")
unique_list = list(set(l1))
print(f"List after removing duplicates: {unique_list}")
new_numbers = [7, 8, 2, 1]
l1 += new_numbers
print(f"List after appending new numbers: {l1}")


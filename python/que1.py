#write a prgrm to find the sum of elements in a list of numbers
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers_list = [1, 2, 3, 4, 5]
result = sum(numbers_list)

print(f"The sum of elements in the list {numbers_list} is:",result)


#input a string and perform the following ops length of the string,rev a string,replace all occurence of the first char with dollar symbol except the first char,input another string concatenate them

input_string1 = input("Enter the first string: ")
string_length = len(input_string1)
reversed_string = input_string1[::-1]
first_char = input_string1[0]
modified_string = first_char + input_string1[1:].replace(first_char, '$')
input_string2 = input("Enter the second string: ")
concatenated_string = input_string1 + input_string2
print(f"Length of the string: {string_length}")
print(f"Reversed string: {reversed_string}")
print(f"Modified string: {modified_string}")
print(f"Concatenated string: {concatenated_string}")

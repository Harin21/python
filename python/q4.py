# Create a dictionary of item numbers and item names
items_dict = {
    101: "Keyboard",
    203: "Mouse",
    305: "Monitor",
    102: "Laptop",
    404: "Headphones",
}

ascending_sorted_items = dict(sorted(items_dict.items(), key=lambda item: item[1]))


descending_sorted_items = dict(sorted(items_dict.items(), key=lambda item: item[1], reverse=True))


print("Original Dictionary:")
print(items_dict)

print("\nSorted Dictionary (Ascending Order of Item Names):")
print(ascending_sorted_items)
print("\nSorted Dictionary (Descending Order of Item Names):")
print(descending_sorted_items)

num = input("Enter Number: ")
sum = 0
for i in num:
    sum = sum + int(i)
print(sum)
temp = num
rev = 0
while(num > 0):
    rem = num % 10
    rev = (rev * 10) + rem
    num = num // 10
print(rev)

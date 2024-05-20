#write a program to find the factorial of a nummber
num = int(input("Enter the number: "))
fact = 1
i = 1
while i <= num:
    fact *=i
    i=i+1
print(fact)    
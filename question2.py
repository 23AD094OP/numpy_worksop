# find if the given number is a palindrome or not?
num = int(input("Enter the number:- "))
temp = num
rev = 0
while num > 0:
    mod = num%10;
    rev = mod + rev*10
    num =num//10
if temp == rev:
    print(temp, "Is a palindrome")
else:
    print(temp,"is not palindrome")        
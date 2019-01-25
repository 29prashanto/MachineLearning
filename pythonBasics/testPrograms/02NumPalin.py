# WAP to Check if a Number is a Palindrome or not?


number = int(input("Enter the number to check for Palindrome: "))

temp = number

reverse = 0

while number > 0:
    digit = number%10
    reverse = reverse*10 + digit
    number = number//10

if (temp == reverse):
    print("Number is a Palindrome number")
else:
    print("Number is NOT a Palindrome number")

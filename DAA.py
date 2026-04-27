#1ST PROGRAM
"""num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")"""

#2ND PROGRAM
"""def square(n):
    return n * n

print(square(5))"""

#3RD PROGRAM
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)"""
#4TH PROGRAM
"""numbers = [10, 20, 30, 40, 50]

total = 0
for num in numbers:
    total += num

print("Sum of the list elements:", total)"""
#5PROGRAM
"""string = input("Enter a string: ")

reversed_string = string[::-1]

print("Reversed string:", reversed_string)"""
#6TH PROGRAM
"""word = input("Enter a word: ")

if word == word[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")"""
#7TH PROGRAM
"""num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")"""
#8TH PROGRAM
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", num, "is", factorial(num))
#9TH PROGRAM 
"""numbers = [10, 25, 30, 45, 60, 75]
key = int(input("Enter the element to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at position:", i)
        found = True
        break

if not found:
    print("Element not found")"""
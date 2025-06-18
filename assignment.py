# A python program that checks whether a number is even or odd

number = int(input("Enter a number :"))

if number == 0:
    print(number, "is neutral")
elif number %2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

print()

# A python program that checks whether a letter is a vowel or consonant

letter = input("Enter a letter :")

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, "is a Vowel")
else:
    print(letter, "is a consonant")

print()

# A python program that returns the perimeter of a rectangle

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

perimeter = 2 * (length + width)

print("perimeter of the rectangle is :",perimeter)

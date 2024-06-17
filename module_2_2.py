first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
third = int(input('Enter the third number: '))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third and first != third:
    print(0)

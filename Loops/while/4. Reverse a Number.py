num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10   # last digit hai ye
    if digit % 2 != 0:   # check kro digit odd hai ya nh
        reverse = reverse * 10 + digit
    num = num // 10   # remove kro last digit ko
    
print("Reversed odd digits:", reverse)
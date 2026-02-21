num = int(input("Enter a positive integer: "))
count = 0

while num > 0:
    digit = num % 10 
    if digit % 2 == 0:
        count += 1
    num = num // 10
    
print("Number of even digits:", count)
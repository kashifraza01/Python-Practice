largest = None

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break   # stop kro jab 0 enter ho
    if largest is None or num > largest:
        largest = num
if largest is not None:
    print("Largest number entered:", largest)
else:
    print("No numbers were entered.")
    
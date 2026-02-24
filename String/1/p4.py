s = input("enter a string: ")
length = len(s)

if length > 8:
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    if first_half == second_half:
        print("Mirror String")
    elif s[0].lower() in "aeiou":
        print(s[1:-1])
    else:
        print(s[::-1])
else:
    print(s.upper())
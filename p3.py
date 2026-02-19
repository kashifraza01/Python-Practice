s = input("enter a string: ")

fchar = s[0].lower()
lchar = s[-1]
length = len(s)
mid = length // 2

vowels = "aeiou"

if fchar.isalpha() and fchar not in vowels:
    if lchar.isdigit():
        # reverse sirf first half ko
        fhalf = s[:mid][::-1]
        shalf = s[mid:]
        print(fhalf + shalf)
    else:
        # reverse sirf second half ko
        fhalf = s[:mid]
        shalf = s[mid:][::-1]
        print(fhalf + shalf)
else:
    print(s.replace(" ", ""))
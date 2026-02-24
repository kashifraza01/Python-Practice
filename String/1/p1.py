s = input("enter a string: ")
length = len(s)
print("hii")

if length > 5:
    mid = length // 2
    fhalf = s[:mid]
    shalf = s[mid:]

    if fhalf == shalf[::-1]:
        print("Palindrome Half")
    elif s.isupper():
        vowels = "AEIOU"
        result = ""
        for ch in s:
            if ch not in vowels:
                result += ch
        print(result)
    else:
        swapped = shalf + fhalf
        print(swapped)
else:
    modified = s[1:]
    print(modified + modified)
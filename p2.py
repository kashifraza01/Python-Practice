s = input("enter a string: ")
length = len(s)

if 6<length<12:
    if s[0] == s[-1]:
        print(s[1:-1])
    elif " " in s:
        print(s.split()[0])
    else:
        print(s[::2])
else:
    print(s[::-1])
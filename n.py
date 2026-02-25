zz=input("enter your name: ")
# has_vowel=False
# for ch in zz:
#     if ch.lower() in "aeiou":
#         has_vowel=True
#         break
# if has_vowel:
#     print("has vowels")
# else:
#     print("doesn't have vowels")

if any(ch in "AEIOUaeiou" for ch in zz):
    print("has vowels")
else:
    print("doesn't has vowels")

b=5
a =b
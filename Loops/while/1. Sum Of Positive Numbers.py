sum=0
while True:
    a=int(input("enter a num: "))
    if a<0:
        break
    if a>0:
        sum+=a
        
print("sum of positive numbers", sum)
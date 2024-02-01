year=int(input("Enter your Number: "))
print(" ")
if year%400==0 or year%4==0 and year%100!=0:
    print(year,"Leap Year")
else:
    print(year,"Not a Leap Year")
#Factorial Number

# i=int(input("Enter your number:"))
# a=1
# while i>0:
#     a=a*i
#     i=i-1
#     print(a)

def rahul(n):
    if n==0 or n==1:
        return 1
    else:
        return n*rahul(n-1)
A=int(input("Enter Your Number:"))
if (A<0):
   	print("Factorial not found")
else:
    print("Factorial Number:",rahul(A))

	
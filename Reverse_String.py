#Revarse String:
      
# a="RAHUL"
# print(a[-1::-1])
def rahul(str):
    size=len(str)
    if (size==0):
        return 0
    last_char=str[size-1]
    print(last_char,end="")
    rahul(str[0:size-1])
str=str(input("Enter String: "))
rahul(str)

# name=input("Enter String:")
# print("Origional string: ",name)
# r_name=""
# for i in char:
#     r_name=i+r_name
# print(r_name)
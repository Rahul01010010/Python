# def Duplicate(List,Key):
#     List2=[]
#     flag=
#     for i in range(len(List)):
#         if Key==List[i]:
#             flag=True
#             List2.append(i)
#     if flag==True:
#         print("Key Element is find a index: ")
#         for i in List2:
#             print(i)
#     else:
#         print("Key is not found")
# List=[1,2,3,5,4,9,25,86,75,15,34,6,1,85,6,1,25,46,9,55,85,26]
# print(List)
# Key=int(input("Enter Your Key: "))
# print(" ")
# Duplicate(List,Key)

def duplicate(List,Key):
    List2=[]
    flag=False
    for i in range(len(List)):
        if Key==List[i]:
            flag=True
            List2.append(i)
    if flag==True:
        print("key element is find a index:")
        for i in List2:
            print(i)
        else:
            print("Key is not found")
List=[10,20,30,50,40,60,80,70,90,25,31,51,43,95,75,85,80,50,46,16,94]
print(List)
print(" ")
Key=int(input("Enter a number: "))
duplicate(List,Key)
        
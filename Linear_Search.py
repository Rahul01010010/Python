def linior(List,Key):
    for i in range(len(List)):
        if Key==List[i]:
            print(" ")
            print("Element Found a Index:",i)
            break
    else:
        print(" ")
        print("Element Not Found ")
    
List=[1,5,9,3,7,8,4,6,15,20,85,65,45,93,26,43,86,92]
print(List)
print(" ")
Key=int(input("Enter a Key Number: "))
linior(List,Key)
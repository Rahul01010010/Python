def rahul(list,key):
    left=0
    righ=len(list)-1
    flag = False
    
    while left<=righ:
        mid=(left+righ)//2
        
        if list[mid]==key:
            flag = True
            print("Index Found At: ",mid)
            break
            
        elif key<list[mid]:
            righ=mid-1
            
        elif key>list[mid]:
            left=mid+1
        
    else:
        print("not found!!")
        
            
list=[10,20,30,40,50]
print(list)
key=int(input("Enter Number: "))
rahul(list,key)
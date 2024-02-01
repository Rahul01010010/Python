def bubble(list):
    Bold='\33[1m'
    n=len(list)
    for i in range(n):
        flag=False
        for j in range(0,n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                flag=True
    print(Bold+"sort list is ",list)
list=[5,9,1,7,3,6,4]
bubble(list)


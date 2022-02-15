list1=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
def show():
    i=0
    a=[]
    co=0
    sum=0
    while i<len(list1):
        if list1[i]>0:
            co=co+1
        elif list1[i]<0:
            sum=sum+list1[i]
        i=i+1
    a.append(co)
    a.append(sum)
    print(a)
show()
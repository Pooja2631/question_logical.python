list1=[1,2,3,4,5,6,7,8,9,10]
def sum():
    i=0
    sum=0
    while i<len(list1):
        square=list1[i]*list1[i]
        sum=sum+square
        i=i+1
    print(sum)
sum()

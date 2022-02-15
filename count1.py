list1=[3,'a','a','a',2,3,'a',3,'a',2,4,9,3,'a','a','a']
i=0
while i<len(list1):
	j=0
	count=0
	while j<len(list1):
		if list1[i]==list1[j]:
			count=count+1
		j=j+1
	i=i+1
print(count)

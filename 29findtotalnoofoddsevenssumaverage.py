list=[1,2,3,4,5,6,7,8,9,10]
count=0
sum=0
count_even=0
sum_even=0
for i in list:
	if(i%2!=0):
		count=count+1
		sum=sum+i
		
	elif(i%2==0):
		count_even=count_even+1
		sum_even=sum_even+i
		

print(count)
print(count_even)
print(sum)
print(sum_even)
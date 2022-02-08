arr=[3,4,2,3,4,6,3]
print(arr)
for i in range(0,len(arr)-1):
	if arr[i]!=0:
		for j in range(i+1,len(arr)):
			if arr[i]==arr[j]:
				arr[j]=0
				
print(arr)

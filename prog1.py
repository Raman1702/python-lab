l1=list(map(int,input().split()))
b=[]
for i in l1:
	if i not in b:
		b.append(i)
for i in b:
	print(i,end=' ')


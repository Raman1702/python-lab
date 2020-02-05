l=[]
while 1:
	item = input("enter the item=")
	l.append(item)
	n=input('do you want continue=')
	if n.lower() == 'n':
		break
l.sort()
print(l)


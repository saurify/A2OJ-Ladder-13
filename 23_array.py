def main():
	n= int(input())
	l=[int(i) for i in input().split()]
	
	l.sort()
	
	mi=l[0]
	ma=l[-1]
	
	io=l.index(0)
	
	nl= io+1
	pl= len(l)-io-1
	
	print(str(1)+' '+ str(mi))
	if pl>0:
		print(*([n-io-1]+l[io+1:]))
		print(*([io]+l[1:io+1]))
	else:
		print(*([2]+l[1:3]))
		print(*([n-3]+l[3:]))
	return 0

if __name__ == '__main__':
	main()

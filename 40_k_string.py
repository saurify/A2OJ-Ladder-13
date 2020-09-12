def stringmaker(k,d,n):
	a=''
	for i in d:
		d[i]=d[i]//n
		a+=i*d[i]
	return a
def main():
	d=dict()
	n=int(input())
	st=input()
	if len(st)%n!=0:
		print(-1)
		return 0
	else:
		k= len(st)//n
	for i in st:
		d[i]= d.get(i,0)+1
	for i in d:
		if d[i]%n!=0:
			print(-1)
			return 0
	print(stringmaker(k,d,n)*n)
	return 0

if __name__ == '__main__':
	main()

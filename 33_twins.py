def main():
	n=int(input())
	a=[ int(i) for i in input().split()]
	a.sort()
	s=sum(a)
	n=len(a)-1
	cur=0
	while n>=0:
		#print(cur,s,n,a)
		if cur+ a[n]>s-a[n]:
			print(len(a)-n)
			return 0
		cur+=a[n]
		s-=a[n]
		n-=1
	return 0

if __name__ == '__main__':
	main()

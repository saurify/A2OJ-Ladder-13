def main():
	n=int(input())
	ar=[int(i) for i in input().split()]
	if ar.count(ar[0])==n:
		return print(0, n*(n-1)//2)
	else:
		return print(max(ar)-min(ar), ar.count(max(ar))*ar.count(min(ar)))
	'''d=dict()
	ar.sort()
	for i in ar:
		d[i]=d.get(i,0)+1
	count=0
	ma=ar[-1]-ar[0]
	for i in ar:
		if i+ma in d:
			d[i]=d[i]-1
			count+=d[i+ma]'''
	print(ma, count)
	return 0
 
if __name__ == '__main__':
	main()

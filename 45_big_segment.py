def main():
	n=int(input())
	ls=[]
	lmin=999999999999999999999999999
	rmax=0
	for i in range(n):
		l,r= [int(j) for j in input().split()]
		lmin=min(l,lmin)
		rmax=max(rmax,r)
		ls.append((l,r))
	if (lmin,rmax) in ls:
		print(ls.index((lmin,rmax))+1)
		return 0
	print(-1)
	return 0

if __name__ == '__main__':
	main()

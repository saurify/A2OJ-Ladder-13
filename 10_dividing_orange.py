def main():
	n,k= [int(i) for i in input().split()]
	s= list(range(1,n*k+1))
	arr=[int(i) for i in input().split()]
	plist=[]
	for i in arr:
		s.remove(i)
	for i in arr:
		plist.append([i]+s[:n-1])
		s[:]=s[n-1:]
	for i in plist:
		print(*i)
	return 0 

if __name__ == '__main__':
	main()

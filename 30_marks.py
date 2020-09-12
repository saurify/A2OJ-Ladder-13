def main():	
	n,m =[int(i) for i in input().split()]
	sstudents=set()
	mlist=[]
	for i in range(n):
		temp=input()
		l=[int(i) for i in temp]
		mlist.append(temp)
	for i in zip(*mlist):
		m= max(i)
		for j in range(n):
			if i[j]==m:
				sstudents.add(j)
	print(len(sstudents))
	return 0

if __name__ == '__main__':
	main()

def main():
	n,k=[int(i) for i in input().split()]
	l=[]
	for i in range(n):
		l.append([int(i) for i in input().split()])
	l.sort(key=lambda x : (-x[0],x[1]))  #x[0] more and x[1] less required, x[1] will be checked if x[0] clashes
	print(l.count(l[k-1]))
	return 0

if __name__ == '__main__':
	main()

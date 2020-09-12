def main():
	n,x=[int(i) for i in input().split()]
	ls= [int(i) for i in input().split()]
	s= sum(ls)
	count=0
	s=abs(s)
	while s>0:
		s-=x
		count+=1
	print(count)
	return 0

if __name__ == '__main__':
	main()

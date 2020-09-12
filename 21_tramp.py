def main():
	n=int(input())
	m=0
	temp=0
	while n:
		a,b=[int(i) for i in input().split()]
		temp+=b-a
		m=max(m,temp)
		n-=1
	print(m)
	return 0

if __name__ == '__main__':
	main()

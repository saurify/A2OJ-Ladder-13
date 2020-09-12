def main():
	n=int(input())
	ar= [int(i) for i in input().split()]
	ar.sort()
	count=0
	for i in range(n):
		count+=abs(ar[i]-i-1)
	print(count)
	return 0

if __name__ == '__main__':
	main()

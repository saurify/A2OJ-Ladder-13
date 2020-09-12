def main():
	n=int(input())
	count=0
	while n:
		P,V,T= [int(i) for i in input().split()]
		if P+V+T>=2:
			count+=1
		n-=1
	print(count)
	return 0

if __name__ == '__main__':
	main()

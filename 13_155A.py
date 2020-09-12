def main():
	n=int(input())
	arr= [int(i) for i in input().split()]
	mi=ma=arr[0]
	count=0
	for i in range(1,n):
		if  arr[i]>ma or arr[i]<mi:
			count+=1
			mi= min(mi,arr[i])
			ma=max(ma,arr[i])
	print(count)			
	return 0

if __name__ == '__main__':
	main()

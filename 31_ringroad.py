def main():
	n,m= [int(i) for i in input().split()]
	#arr= [int(i) for i in input().split()]
	count=0
	last=1
	for i in input().split():
		k=int(i)
		if k>=last:
			count+= k-last
		else:
			count+=n-last+k
		last=k
	print(count)
	return 0

if __name__ == '__main__':
	main()
  

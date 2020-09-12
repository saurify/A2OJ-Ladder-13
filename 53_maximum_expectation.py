def main():	
	m,n=map(int,input().split())
	ans=0
	for i in range(1,m+1):
		ans += (pow(i / m, n) - pow((i-1) / m, n)) * i 
	print(ans)
	return 0

if __name__ == '__main__':
	main()

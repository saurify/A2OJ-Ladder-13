def main():
	n,m = [int(i) for i in input().split()]
	print(max(m,n)-1 ,min(n,m))		#only cases where game is played optimally well	
	return 0

if __name__ == '__main__':
	main()

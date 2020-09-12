def main():
	n=int(input())
	
	def checker(a):
		l=list(str(a))
		s=set(l)
		if len(s)==len(l):
			return 1
		return 0
		
	while 1:
		n+=1
		if checker(n):
			print(n)
			return 0
	
	return 0

if __name__ == '__main__':
	main()

def main():
	n=int(input())
	s= input()
	count=0
	i=1
	while i<n:
		if s[i-1]==s[i]:
			count+=1 
		i+=1
	print(count)
	return 0

if __name__ == '__main__':
	main()

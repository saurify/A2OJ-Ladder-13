def main():
	n,t= [int(i) for i in input().split()]
	inn=input()
	seq=[char for char in inn]
	while t:
		i=0
		while i<n:
			if i<n-1:
				if seq[i]=='B' and seq[i+1]=='G':
					seq[i], seq[i+1]= seq[i+1], seq[i]
					i+=1
					
			i+=1
		t-=1
	s=''
	for i in seq:
		s+=i
	print (s)
	return 0

if __name__ == '__main__':
	main()

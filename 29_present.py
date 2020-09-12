def stringgen(n):
	s=''
	for i in range(n+1):
		s+=str(i)+' '
	j=s[:-1]
	for i in reversed(range(0,n)):
		j+=' ' + str(i)
	return j
	
def main():
	n=int(input())
	l=2*n+1
	for i in range(n+1):
		cur= 2*i+1
		spaces= (l-cur)
		s=' '*spaces+ stringgen(i)
		print(s)
	for i in reversed(range(n)):
		cur= 2*i+1
		spaces= (l-cur)
		s=' '*spaces+ stringgen(i)
		print(s)
		
	return 0

if __name__ == '__main__':
	main()

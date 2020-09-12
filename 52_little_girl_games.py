def main():
	s=input()
	st=( i for i in s)
	k=0
	for i in st:
		if s.count(i)%2:
			k+=1
	if k<=1 or (k>1 and k%2==1) :
		print('First')
		return 0
	if k%2==0:
		print( 'Second')
		
	return 0

if __name__ == '__main__':
	main()

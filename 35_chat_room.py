def main():
	s='hello'
	n=0
	for i in input():
		if n<5 and i==s[n]:
			n+=1
	if n==5:
		print('YES')
		return 0
	print('NO')
	return 0

if __name__ == '__main__':
	main()

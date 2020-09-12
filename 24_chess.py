def main():
	n=8
	while n:
		r=input()
		for i in range(7):
			if r[i]==r[i+1]:
				print('NO')
				return 0
		n-=1
	print('YES')
	return 0

if __name__ == '__main__':
	main()

def main():
	lucky=[4,7,47,74,444,447,474,477,744,747,777]
	n=int(input())
	for i in lucky:
		if n%i==0:
			print('YES')
			return 0
	print('NO')
	return 0

if __name__ == '__main__':
	main()

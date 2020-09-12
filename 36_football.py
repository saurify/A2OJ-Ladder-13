def main():
	mc=0
	s=input()
	for i in range(len(s)-1):
		#print(s[i], s[i+1], mc)
		if s[i]==s[i+1]:
			mc+=1
			if mc>=6:
				print('YES')
				return 0
		else:
			mc=0
	print('NO')
	return 0

if __name__ == '__main__':
	main()

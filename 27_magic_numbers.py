def main():
	n=input()
	for i in n:
		if n[0]=='4':
			print("NO")
			return 0
		if '444' in n:
			print('NO')
			return 0
		if i!='4' and i!='1':
			print('NO')
			return 0
	print('YES')
	return 0

if __name__ == '__main__':
	main()

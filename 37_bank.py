def main():
	n=input()
	if int(n)<0:
		if int(n[:-1])>int(n[:-2]+n[-1]):
			print(int(n[:-1]))
		else:
			print(int(n[:-2]+n[-1]))
		return 0
	print(n)
	return 0

if __name__ == '__main__':
	main()

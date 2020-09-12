def main():
	str1= raw_input()
	str2= raw_input()
	scramble= raw_input()
	if sorted(str1+str2)==sorted(scramble):
		print ('YES')
		return 0
	else:
		print('NO')
	return 0
if __name__ == '__main__':
    main()

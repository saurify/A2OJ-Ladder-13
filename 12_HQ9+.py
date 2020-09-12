
def main():
	in1= input()
	for i in in1:
		if i in 'HQ9':		#no output on +, only internal value changes
			print('YES')
			return 0
	print('NO')
	return 0
	
if __name__ == '__main__':
	main()

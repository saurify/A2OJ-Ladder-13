

def main():
	n= input()
	arr=raw_input()
	s=0
	for i in arr.split():
		s+= int(i)
	print(s*1.0/n*1.0)
	return 0
if __name__ == '__main__':
	main()

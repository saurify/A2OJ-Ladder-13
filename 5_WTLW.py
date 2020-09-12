
def main():
	n=input()
	words=[]
	for i in range(n):
		in1= raw_input()
		words.append(in1)
	for i in words:
		if len(i)>10:
			print(i[0]+str(len(i)-2)+i[-1])
		else:
			print(i)
	return 0

if __name__ == '__main__':
	main()

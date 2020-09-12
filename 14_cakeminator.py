
def main():
	r,c= [int(i) for i in input().split()]
	erow=[]
	ecol=[]
	count=0
	for i in range(r):
		s=input()
		for col in range(c):
			if s[col]=='S':
				erow.append(i)
				ecol.append(col)	

	for i in range(r):
		for j in range(c):
			
			if i in erow and j in ecol:
				pass
			else:
				count+=1
	print(count)
				
	return 0

if __name__ == '__main__':
	main()

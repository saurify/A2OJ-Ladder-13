def main():
	s, n= [int(i) for i in input().split()]
	c=0
	l=[]
	for i in range(n):
		l.append([int(i) for i in input().split()])
	l.sort(key=lambda x: x[0])
	for i in l:
		if i[0]<s:
			s+=i[1]
			c+=1
	if c==n:
		print('YES')
		return 0
	print('NO')		
	return 0

if __name__ == '__main__':
	main()

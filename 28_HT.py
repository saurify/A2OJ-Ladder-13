def main():
	x,y,a,b=[ int(i) for i in input().split()]
	l=[]
	count=0
	for i in range(a,x+1):
		for j in range(b,y+1):
			if i>j:
				count+=1
				l.append([i,j])
	print(len(l))
	for i in l:
		print(*i)
	return 0

if __name__ == '__main__':
	main()

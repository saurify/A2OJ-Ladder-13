def main():
	y,k,n=[int(i) for i in input().split()]
	x= 0
	s=0
	l=[]
	while s<=n:
		if s%k==0:
			
			s+=k
			x=s-y
			if x>0 and s<=n:
				l.append(x)
			pass
		else:
			x+=1
	
	print(*l) if len(l)>0 else print(-1)
	return 0

if __name__ == '__main__':
	main()

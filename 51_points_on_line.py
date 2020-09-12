'''def dist(i,ar,d):
	k=0
	for j in ar[i+1:]:
		if j-ar[i]<=d:
			k+=1			#TLE
		else:
			break
	return k*(k-1)//2'''
def main():
	n,d=map(int,input().split())
	ar=sorted(list(map(int, input().split())))
	ans=0
	l=0
	r=1
	k=0
	while r<n:
		if ar[r]- ar[l]<=d:
			r+=1
			k+=1
			ans+=k*(k-1)//2
		else:
			l+=1
			k-=1
		
	'''for i in range(n):
		ans+=dist(i,ar,d)'''
	print(ans)
	
	return 0

if __name__ == '__main__':
	main()

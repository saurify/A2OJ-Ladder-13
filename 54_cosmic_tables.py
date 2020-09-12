'''def colchanger(l,x,y,n):
	for i in range(n):
		l[i][x-1],l[i][y-1]=l[i][y-1], l[i][x-1]

def rowchanger(l,x,y,m):
	for i in range(m):
		l[x-1][i],l[y-1][i]=l[y-1][i], l[x-1][i]'''

def main():
	'''n, m, k = map(int, input().split())
	R = {str(i): i - 1 for i in range(n+1)}
	C = {str(i): i - 1 for i in range(m+1)}
	ans = []
	l = [input().split() for i in range(n)]
	for i in range(k):
		q, x, y = input().split()
		if q == 'c':
			C[x], C[y] = C[y], C[x]
		elif q == 'r':
			R[x], R[y] = R[y], R[x]
		else:
			ans.append(l[R[x]][C[y]])
	print('\n'.join(ans))'''
	n,m,k = map(int, input().split())
	l=[]
	for i in range(n):
		l.append(list(map(int, input().split())))
	#q=[]
	r=dict()
	c=dict()
	#for zzz in range(k):
	#	s,x,y= [i for i in input().split()]
	#	q.append([s, int(x),int(y)])
	for j in range(k):
		s,a,b= input().split()
		
		if s=='g':
			print(l[int(r.get(a,a))-1][int(c.get(b,b))-1])
		elif s=='r':
			r[a],r[b]=r.get(b,int(b)),r.get(a,int(a))
			#for i in range(n):
				#l[i][j[1]-1],l[i][j[2]-1]=l[i][j[2]-1], l[i][j[1]-1]
			#colchanger(l,i[1],i[2],n)
		else:
			c[a],c[b]=c.get(b,int(b)),c.get(a,int(a))
			#for i in range(m):
				#l[j[1]-1][i],l[j[2]-1][i]=l[j[2]-1][i], l[j[1]-1][i]
			#rowchanger(l,i[1],i[2],m)
	
		
	return 0

if __name__ == '__main__':
	main()

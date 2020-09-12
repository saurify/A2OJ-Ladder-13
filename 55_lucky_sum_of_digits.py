n=int(input())

# n=4*a + 7*b  4......(a times)  7......(b times)   mc is minimum value of a+b
b, a, mc=0, 0, [99999999999,0,0]
s= a*4 + b*7
d=99999999999
while s<=n:
	b=(n-a*4)//7
	
	s= a*4 + b*7
	d=min(a+b,mc[0])
	#print('wtf   is going on,',a,b,d,s,mc) 
	if d!=mc[0] and s==n:
		mc=[d,a,b]
	a+=1
	if a<0 or b<0:
		break
		
print('4'*mc[1]+'7'*mc[2] if mc[1]>0 or mc[2]>0 else -1)
	

def main():
	n=int(input())
	a=[int(i) for i in input().split()]
	s=dict()
	for i in a:
		if i==25:
			s[25]=s.get(25,0)+1
			pass
		if i==50:
			if s.get(25,0)>0:
				s[25]-=1
				s[50]=s.get(50,0)+1
				pass
			else:
				print('NO')
				return
		if i==100:
			if s.get(50,0)>0 and s.get(25,0)>0:
				s[50]-=1
				s[25]-=1
				pass
			elif s.get(25,0)>2:
				s[25]-=3
				pass
			else:
				print('NO')
				return

	print('YES')
	return 0

if __name__ == '__main__':
	main()

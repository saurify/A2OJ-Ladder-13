def main():
	

	import sys
	sys.stdin = open("input.txt")
	sys.stdout = open("output.txt",'w')
    
	a,b=[int(i) for i in input().split()]
	ans=''
	if a < b:
		ans+='GB'*a+'G'*(b-a)
	else:
		ans+='BG'*b+'B'*(a-b)
	print(ans)
	

if __name__ == '__main__':
	main()

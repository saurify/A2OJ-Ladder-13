

def main():
	n,k= [int(i) for i in input().split()]
	joy=-9999999999999

	for i in range(n):
		f,t = [int(i) for i in input().split()]
		if t<k:
			temp=f
		elif t>=k:
			temp=f+k-t
		joy=max(joy,temp)
	print(joy)
	return 0
	
if __name__ == '__main__':
	main()

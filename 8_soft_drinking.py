
def main(args):
	n,k,l,c,d,p,nl,np= [int(i) for i in input().split()]
	print( min((k*l)//nl, c*d,p//np)//n)
	return 0 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

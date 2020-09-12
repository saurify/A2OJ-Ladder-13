def main():
	import math
	#x= A x B	y= B x C 	z= C x A
	x,y,z= [int(i) for i in input().split()]
	p=x*y*z
	print(round(4*(math.sqrt(p//(x*x))+ math.sqrt(p//(y*y))+ math.sqrt(p//(z*z)))))
	return 0

if __name__ == '__main__':
	main()

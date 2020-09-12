def main():
	n = input()
	arr= raw_input()
	arr=arr.split()
	temp=dict()
	for i in range(n):
		arr[i]= int(arr[i])-1
		temp[arr[i]]=i
	for i in range(n):
		arr[i]= temp[i]+1
	print ' '.join([str(x) for x in arr]) 
	return 0

if __name__ == '__main__':
	main()

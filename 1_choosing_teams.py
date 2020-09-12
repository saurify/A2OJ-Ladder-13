def main():
	in1= raw_input()
	in2= raw_input()
	n,k=int(in1.split()[0]), int(in1.split()[1])
	students=in2.split()
	for i in range(len(students)):
		students[i]= int(students[i])
	students.sort()
	trav=2
	ans=0
	allowed= 5-k
	while trav<len(students):
		#print(students[trav],allowed)
		if students[trav]<=allowed:
			ans+=1
		trav+=3	
	
	print(ans)
	return ans


if __name__ == '__main__':
	main()

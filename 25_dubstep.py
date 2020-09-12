def main():
	s=input()
	i=0
	ans=''
	while i<len(s):
		#print(s[i:])
		if i+3<=len(s) and s[i:i+3]=='WUB':
			i+=3
			ans+=' '
			pass	
		else:
			ans+=s[i]
			i+=1
	#print('initial', ans)
	ans=' '.join(list(ans.split()))
	print(ans)
	return 0

if __name__ == '__main__':
	main()

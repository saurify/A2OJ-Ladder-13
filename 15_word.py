def main():
	w=input()
	scount=0
	ccount=0
	for i in w:
		if ord(i)>=ord('a') and ord(i)<=ord('z'):
			scount+=1
		if ord(i)>=ord('A') and ord(i)<=ord('Z'):
			ccount+=1
	#print(ccount, scount)
	print(w.upper()) if scount<ccount else print(w.lower())
	return 0

if __name__ == '__main__':
	main()

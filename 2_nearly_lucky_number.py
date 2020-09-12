def main():
    num= input()
    cnt=0
    for i in str(num):
    	if i=='7' or i=='4':
    	    cnt+=1
    
    if cnt==4 or cnt==7:
    	print('YES')
    	return 0
    for i in str(cnt):
        if i!='7' and i!='4':
            print('NO')
            return 0
    print('YES')
    return 0
if __name__ == '__main__':
    main()

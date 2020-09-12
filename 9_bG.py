
def main():
	u=str(input())
	cs=set()
	for i in u:
		cs.add(i)
	if len(cs)%2:
		print('IGNORE HIM!')
	else:
		print('CHAT WITH HER!')
	return 0
if __name__ == '__main__':
	main()

def main():
	a=input().lower()
	b=input().lower()
	if a>b:
		print(1)
		return 0
	if a==b:
		print(0)
		return 0
	if a<b:
		print(-1)
	return 0

if __name__ == '__main__':
	main()

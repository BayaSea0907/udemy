

file1 = open('test.txt', 'r')
print('file1=open')
print(file1.readline())

with open('test.txt', 'r') as file2:
	print('with open as file2')
	print(file2.read(7))

file1.close()


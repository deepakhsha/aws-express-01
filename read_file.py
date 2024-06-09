#read contents from file and display in console
file_path = input('Enter file path: ')
file = open(file_path,'r')
print(file.read())
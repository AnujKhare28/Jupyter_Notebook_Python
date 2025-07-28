# Write Mode

file = open('mode.txt', 'w')

file.write('Hello!!\n')
file.write('My name is Anuj Khare!!\n')

# Append Mode

file = open('mode.txt', 'a')
file.write('I am learning Python!!\n')

# Read and Write Mode

file = open('mode.txt', 'r+')
str1 = file.read(29)
print(str1)
file.write('Good Bye!!!!\n')


file.close()
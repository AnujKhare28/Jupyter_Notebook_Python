f = open('Orange.png', 'rb')

data = f. read()

cp = open('Orange_copy.png', 'wb')

cp.write(data)

f.close()
cp.close()
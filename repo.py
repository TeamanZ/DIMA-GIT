f = open('text.txt','r')
a = f.read()
c = len(f.read())
key = 1
crypt = ""
for i in a:
    try:
        crypt += chr(ord(i) ^ ord(key))
    except TypeError:
        crypt += chr(ord(i) ^ key)
with open("out.txt", "w") as file:
        file.write(crypt)
        file.close()
f.close()
print(crypt)

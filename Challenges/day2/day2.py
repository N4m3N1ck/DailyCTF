s = input()
x = ""
for i in range(len(s)):
	x += str(hex(ord(s[i])+69-i))[2:]
print(x)	

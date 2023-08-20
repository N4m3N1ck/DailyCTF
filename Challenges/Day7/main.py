# c: ěĒęğķĦçČáÌõ
# https://www.youtube.com/watch?v=-tJYN-eG1zki
def encrypt(msg,key):
	c = ""
	for i in range(len(msg)):
		c += chr(ord(msg[i])+ord(key[i])+69)
	return c

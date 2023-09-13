def encrypt23(s):
    encrypted = s[0]
    for i in range(1, len(s)):
        encrypted += str(ord(s[i])-ord(s[i-1]))
    return encrypted
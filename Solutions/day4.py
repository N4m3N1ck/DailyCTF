from hashlib import sha256
wordlist = '''P@ssw0rd!123
Secur3Pa$$word
Ch@ll3nge_2023
CTF_R0cks!
3xp10reTh3Fl@g
H@ckTh3Cod3!
D3c0d3M3Now
Br@1n_Tw1st!
CTF_Champ_23
Puzzl3Mast3r
H@ck3rHunt$%
R3v3rs3_Th1s!
EncryptMePlz
J0inTh3Qu3st
CrackTh1s!
P@ssw0rdPuzzl3
Ch@ll3ngeAcc3pt
Unl0ck_M3!
R3s0lv3M3N0w
P@ssw0rdN1nj@
Br@1n_T3as3r
C0d3Br34k3r
Ex0ticP@ssw0rd
CTF_Master_23
DecipherM3!
H@ck3r$Un1t3d
3nigmaS0lv3r
G3n1us_C0d3!
Th3_P@ss_K1ng
Qu3st4Gl0ry
Cr@ckM3N0w!
Inspect_Th1s
Pr0t3ct_M3!
P@ssw0rdHunt3r
Ch@ll3ng3MePlz
Mys7eryC0d3
H@ck3rHaven
D3cryptTh1s!
Secur3_Cod3$
Br@1nT3st3r
CTF_Champ_2023
R1ddl3M3N0w
Unr@velTh1s!
P@ssw0rdMyst3ry
Qu3stM@st3r
H@ck3r$Qu3st
Ech0_Th3Cod3
C0d3Slu3th
3nigmaUnv34led
Pr0t3ct_M3Plz
Ch@ll3ng3S0lv3r
M3ssag3Fr0mMars
P@ssw0rdGuru
Br@1n_T3stM3
CTF_Hunt3r_23
R3v3alTh1sC0d3
Qu3st_Enthusi@st
C0d3Br34k3r_2023
H@ck3r'sC0d3
D3c0d3M3Plz
Ech0_Th3M3ss@ge
P@ssw0rd_Wiz@rd
Br@1n_T3stCh@mp
CTF_Myst3ry
Pr0t3ctTh3C0d3
H@ck3r_Haven_23
M@keM3S3cur3
Unveil_Th1s!
Ch@ll3ng3_Awaits
P@ssw0rd_V@ult
Qu3stCr@cker
C0d3_Cr3@tor
H@ck3r$L@ir
D3c0d3_MySecr3t
Br@1n_T3stGuru
R3v3al_Th3K3y
CTF_Ch@ll3ng3r
Enigm@S0lv3r
Pr0t3ctTh1sC0d3
H@ck3r$N3twork
Intr1gu3M3!
P@ssw0rd_W0rld
Br@1n_T3stG3n1us
CTF_Ch@mp_2023!
R3v3al_Th3S3cr3t
M@ster_Th3C0d3
H@ck3r$H@v3n_23
Ch@ll3ng3_Invit3
Cr@ck_M3N0w!
P@ssw0rd_K1ngd0m
Qu3stM@st3r_23
C0d3_Unr@v3l
H@ck3r$L@ir_2023
D3c0d3_Th3H1nt
Br@1n_T3stM@st3r
CTF_Myst3ry_23
Pr0t3ct_Th3K3y
H@ck3r$Pl@yground
Enigm@D3c0d3r
P@ssw0rd_Enigma'''
for i in wordlist.split():
	if sha256(i.encode('utf-8')).hexdigest() == "593c3d4a5042baf46089a8cfa6f1bd6e33766b84fc303f0f041e86d0957bb35a":
		print(i)

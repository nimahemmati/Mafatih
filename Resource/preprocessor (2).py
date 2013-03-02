fin = open("PlainText_V1.htm", "r+")
lines = fin.readlines()
fin.close()
out = open("Babe1.htm", "a")
for i in range(32, 13638):
	out.write(lines[i])
out.close()
out = open("Babe2.htm", "a")
for i in range(13639 , 30170):
	out.write(lines[i])
out.close()
out = open("Babe3.htm", "a")
for i in range(30171 , 50983):
	out.write(lines[i])
out.close()
out = open("Khateme1.htm", "a")
for i in range(50984 , 51527):
	out.write(lines[i])
out.close()
out = open("Molhaghate1.htm", "a")
for i in range(51528 , 53645):
	out.write(lines[i])
out.close()
out = open("Molhaghate2.htm", "a")
for i in range(53646 , 65669):
	out.write(lines[i])
out.close()
out = open("Khateme2.htm", "a")
for i in range(65670 , 67071):
	out.write(lines[i])
out.close()
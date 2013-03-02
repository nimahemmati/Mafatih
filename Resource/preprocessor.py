fin = open("AllFile.htm", "r+")
text = fin.read()
fin.close()
size = len(text)
while True:
	end = -1
	start = text.find('<h3 align="center">', end + 1)
	end = text.find("</h3>", start + 5)
	text = text.replace(text[start:end], "")
	print start
	print len(text)
	if start == -1:
		break

while True:
	end = -1
	start = text.find('<div align="center">', end + 1)
	end = text.find("</div>", start + 6)
	text = text.replace(text[start:end], "")
	print start
	print len(text)
	if start == -1:
		break
while True:
	end = -1
	start = text.find('<center>', end + 1)
	end = text.find("</center>", start + 9)
	text = text.replace(text[start:end], "")
	text = text.replace('<p>&nbsp;</p>', "")
	text = text.replace('<br>', "")
	text = text.replace('&nbsp;', "")
	text = text.replace('<blockquote>', "")
	text = text.replace('</blockquote>', "")
	text = text.replace('<p align="center">', "")
	print start
	print len(text)
	if start == -1:
		break
	
	
		

out = open("AllFile1.htm", "w")
out.write(text)
out.close()

#<p class="RedT">&nbsp;</p>
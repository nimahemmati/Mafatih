import os
import glob
import os
import ntpath
os.chdir("./")
documents ='<html dir="rtl"><head><meta content="text/html" charset="utf-8" http-equiv="Content-Type"></head><body>'
for files in glob.glob("*.htm"):
  filename =  ntpath.abspath(files)
  textFile = open( files , "r")
  text = textFile.read()
  textFile.close()
  end = -1
  start = text.find("<blockquote>", end+1)
  end = text.find("</blockquote>",start+1)
  documents+=(text[start:end])
documents+= '</body></html>'
os.chdir("E:\\Personal\\Projects\\Mafatih\\Aviny - Test\\Result")
out = open("AllFile.htm", "w")
out.write(documents)
out.close()

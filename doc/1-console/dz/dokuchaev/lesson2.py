import os
import shutil


listdir = os.listdir("./tmp")
i = 0
for files in listdir:
	dirname =  "./tmp/" + files
	print(dirname)
	shutil.move("%s" % (dirname) , "./dir2") 
	i+=1
	

    

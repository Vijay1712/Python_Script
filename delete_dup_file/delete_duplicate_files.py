import os
import glob




#get all sub diretories 

root = 'C:\\Users\\Vijayendra Jagtap\\Desktop\\practice'
subdirectory = []
	for d in os.listdir(root):
		if os.path.isdir(d):
			subdirectory.append(d)


#get each file from a subdirectory and print
files = []
for i in subdirectory:
	subdir = 'C:\\Users\\Vijayendra Jagtap\\Desktop\\practice\\'+i	
	for d in os.listdir(subdir):
 		if ".txt" in d:
 			files.append(d)


# String b;
# for a in files[0]:
# 	b +=a


a = 'C:\\Users\\Vijayendra Jagtap\\Desktop\\practice'
for f in os.listdir(a):
	if ".txt" in f:
		if f in files:
			os.remove(a+ '\\'+f)
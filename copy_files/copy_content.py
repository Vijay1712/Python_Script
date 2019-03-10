import os
import glob

#get all sub diretories 
def copy_files():
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
 					print(d)
 					text_file = open(d, "r")
 					newfile = open("hello", "w+")
 					newfile.write(text_file.read())
 					text_file.close()
			
			
			
 if __name__ == "__main__":
    copy_files()		    




 		  
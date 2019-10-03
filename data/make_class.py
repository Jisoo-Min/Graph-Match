#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 

def get_file_name():
	pass

def main():
	#https://github.com/mirandaio/codingbat
	path = "codingbat-master/java/"
	dirs = os.listdir(path)

	data_list = open("data_list", 'a')
	for folder_name in dirs:
		print("folder: ", folder_name)
		files_list = os.listdir("codingbat-master/java/" + folder_name)
		for file_name in files_list:

			file = open("codingbat-master/java/" + folder_name + "/" + file_name, "r")
			begin = "class " + folder_name.title().replace("-", "") + file_name[:-5].title() + "{ \n"

			codes = file.readlines()  # Get codes
			codes.insert(0, begin)    # Add it 
			file.close()

			new_file = open("codingbat-data/" + folder_name.title().replace("-", "") + file_name[:-5].title() + ".java", "a")
			new_file.writelines(codes)
			new_file.write("}")
			new_file.close()


			data_list.write(folder_name.title().replace("-", "") + file_name[:-5].title() + "\n")
	print(dirs)



if __name__ == "__main__":
	main()
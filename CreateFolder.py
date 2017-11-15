import os

def create_folder():
	try:
		# save name of new folder
		fld_name = str("Folder " + (raw_input("Folder Name: ")))
		# if folder name exist, try anotherone
		while os.path.exists(fld_name):
			print "Folder name already exists"
			fld_name = str("Folder " + (raw_input("Folder Name: ")))
		# if folder name not exist, save new folder
		if not os.path.exists(fld_name):
			os.makedirs(fld_name)
			print "New folder created: " + fld_name
	except OSError as e:
		print e
	return fld_name
  
if __name__ == "__main__":
    new_folder = create_folder()
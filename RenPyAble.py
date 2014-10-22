# renpyable.py - Simple python programm to reneame TIF files 
# (generated from Trueflow RIP) for better sort ability.
# Author: propbono
# E-mail: propbono@gmail.com
#

import os
import operator
import datetime
from config import RealConfig
from config import FakeConfig

class Renpyable:
	def __init__(self, config):
		"""
			Initialization method
			creates and assign neccessary values from configuration file.
			tif_directory - directory where tiff files are stored
			doa_directory - whole disk with customers jobs where *Doa.pdf files are stored
			ppf_directory - directory where cip3 (ppf) files are stored
			pdf_to_ppf_directory - directory where pdf files used to create ppf files are stored
			version - variable responsible for keeping version program
		"""
		self.version = config.VERSION
		self.tif_directory = config.TIF_DIRECTORY
		self.doa_directory = config.DOA_DIRECTORY
		self.ppf_directory = config.PPF_DIRECTORY
		self.pdf_to_ppf_directory = config.PDF_ARCHIVE_DIRECTORY
			
	def create_test_files(self, number):
		"""
			Temporary create method for testing purposes
			Creates neccessary files to test other functions
			Without messing up real files
		"""
		if os.path.exists(self.tif_directory):
			self.delete_test_files()

		# Create directories for fake test files
		os.makedirs(self.tif_directory,mode=0o777,exist_ok=True)
		os.makedirs(self.pdf_to_ppf_directory,mode=0o777,exist_ok=True)
		os.makedirs(self.ppf_directory,mode=0o777,exist_ok=True)
		os.makedirs(self.doa_directory,mode=0o777,exist_ok=True)

		for i in range(1, number + 1):
			# Tif test files
			i_string = str(i) # conversion from int to str
			name1 = "Tif_Test_file_n" + i_string + "_FRONT.tif"
			name2 = "Tif_Test_file_n" + i_string + "_FRONT_K.tif"
			name3 = "Tif_Test_file_n" + i_string + "_BACK.tif"
			name4 = "Tif_Test_file_n" + i_string + "_BACK_K.tif"
			file1 = open(self.tif_directory + name1, 'a')
			file1.close()
			file2 = open(self.tif_directory + name2, 'a')
			file2.close()
			file3 = open(self.tif_directory + name3, 'a')
			file3.close()
			file4 = open(self.tif_directory + name4, 'a')
			file4.close()
			
			# Pdf test files
			name5 = "Pdf_Test_file_n" + i_string.zfill(3) + ".pdf"
			file5 = open(self.pdf_to_ppf_directory + name5, 'a')
			file5.close()
			
			# Ppf test files
			name6 = "Ppf_Test_file_n" + i_string.zfill(3) + ".ppf"
			file6 = open(self.ppf_directory + name6, 'a')
			file6.close()
			
			# DoA test files
			name7 = "Doa_Test_file_n" + i_string.zfill(3) + "_DoA.pdf"
			file7 = open(self.doa_directory + name7, 'a')
			file7.close()
				
	def delete_test_files(self):
		"""
			Temporary delete method.
			Deletes all temporarly created test files
			Oposite to create_test_files method
		"""
		for tif in os.listdir(self.tif_directory):
			os.remove(self.tif_directory + tif)
		for pdf in os.listdir(self.pdf_to_ppf_directory):
			os.remove(self.pdf_to_ppf_directory + pdf)
		for ppf in os.listdir(self.ppf_directory):
			os.remove(self.ppf_directory+ppf)
		for doa in os.listdir(self.doa_directory):
			os.remove(self.doa_directory+doa)

		os.removedirs(self.tif_directory)
		os.removedirs(self.pdf_to_ppf_directory)
		os.removedirs(self.ppf_directory)
		os.removedirs(self.doa_directory)

	# Try to use str.zfill(3) method
	def correct_numbers(self, digits):
		"""
			Try to use str.zfil(3) method
			Function for repair file numbering					
			i.e. 01 in exchange for 1, 02 in exchange 2 ...						
															
			digits		- how many digits will have new		
						  number: 2 - 01, 3 - 001, etc.
		"""
		for digit in range(1, int(digits) + 1):
			print("\n############################################################")
			print("#	Changing numbers - LOOP NO. ", digit, "			   #")
			print("############################################################\n\n")
			tif_file_list = os.listdir(self.tif_directory)
			for f in tif_file_list:
				print("	File: ", f)
				print("	----------------------------------------------------")
				self.replace_number_for_string(f, "FRONT", digit)
				self.replace_number_for_string(f, "FRONT_K", digit)
				self.replace_number_for_string(f, "BACK", digit)
				self.replace_number_for_string(f, "BACK_K", digit)
				print("	----------------------------------------------------\n")
		
	def replace_number_for_string(self, name, search, digits):
		"""
			Helper function which change old name for new name
			with proper number.										
																
			name	-	file name from tif_file_list list		
			search	-	a string which are helping to locate	
						number in the file name					
			digits	-	a number of digits in new number	
		"""
		if operator.contains(name, "A" + search):
			search = "A" + search
			print("		Change: No\n")

		if name.endswith(search, 0, len(name) - 4):
			begin = -4 - len(search) - 1 - digits
			end = -4 - len(search) - 1
			if (not name[begin:end].isdigit()):
				new_name = name[:begin + 1] + "0" + name[end - digits + 1:]
				print("		Change: Yes")
				print("		New Name: ", new_name, "\n")
				os.rename(self.tif_directory + name, self.tif_directory + new_name)
			else:
				print("		Change: No")

	def correct_names(self):
		"""
			Function which correct TIFF files name:						
			This function search for file which ends with "FRONT" or 	
			"FRONT_K" string and put before this string letter "A"																				
		"""
		tif_file_list = os.listdir(self.tif_directory)
		print("\n############################################################")
		print("#	Changing names - FRONT => AFRONT 		   #")
		print("############################################################\n\n")
		for f in tif_file_list:
			print("	File: ", f)
			print("	----------------------------------------------------")
			if operator.contains(f, "AFRONT") or operator.contains(f, "BACK"):  # run time: 1 - 0.314, 2 - 0.115
				print("		Change: No\n")
				continue
			else:
				if f.endswith("FRONT", 0, len(f) - 4):
					new_name = f[:-9] + "A" + f[-9:]
					os.rename(self.tif_directory + f, self.tif_directory + new_name)
					print("		Change: Yes")
					print("		New Name: ", new_name, "\n")
				elif f.endswith("FRONT_K", 0, len(f) - 4):
					new_name = f[:-11] + "A" + f[-11:]
					os.rename(self.tif_directory + f, self.tif_directory + new_name)
					print("		Change: Yes")
					print("		New Name: ", new_name, "\n")
			print("	----------------------------------------------------\n")

	# Here i must use os.walk()
	def delete_unused_DoA_files(self):
		pass

	# tif_file_list = os.listdir(directory)
	# for f in tif_file_list:
	# print()

	def delete_old_ppf_files(self):
		ppf_file_list = os.listdir(self.ppf_directory)
		for f in ppf_file_list:
			modification_date = self.get_modification_time(self.ppf_directory+f)
			
			try:
				today_date = datetime.date.today()
				delete_treshold_date = datetime.date(today_date.year, today_date.month-1,today_date.day)
			except:
				delete_treshold_date = today_date
				
			if(modification_date <= delete_treshold_date):
				print('{0:20} ==> {1} ==> {2} ==> {3}'.format(f, modification_date, delete_treshold_date, "deleted!"))
				os.remove(self.ppf_directory+f)

	def delete_old_pdf_to_ppf_files(self):
		pdf_to_ppf_file_list = os.listdir(self.pdf_to_ppf_directory)
		for f in pdf_to_ppf_file_list:
			print(f)
			
	def get_modification_time(self, filename):
		time = os.path.getmtime(filename)
		return datetime.date.fromtimestamp(time)

if __name__ == "__main__":
	# global variable for checking while loop
	answer = 0
	# change to RealConfig() for production
	renpyable = Renpyable(FakeConfig())
	
	while answer < 9:
		print()
		print("TIFF name changer v.", renpyable.version)
		print("This programm let you change name of TIF files generated by Trueflow.\nChoose what do you want to do:\n")
		print("1. Numbers correction i.e. 1 = 1, 2 = 02, 3 = 003 etc.")
		print("2. Name correction FRONT = AFRONT")
		print("3. Chain points 1, 2 ")
		print("4. Delete unused *DoA.pdf files")
		print("5. Delete > 2 month-old *.ppf files")
		print("6. Delete > 2 month-old *.pdf to *.ppf files")
		print("7. Generate test files")
		print("8. Delete test files")
		print("9. Exit program.")
		answer = int(input("Choose : "))
		
		if answer == 1:
			digits = input("How many digits will have new number?: ")
			renpyable.correct_numbers(digits)
		elif answer == 2:
			renpyable.correct_names()
		elif answer == 3:
			digits = input("How many digits will have new number?: ")
			renpyable.correct_numbers(digits)
			renpyable.correct_names()
		elif answer == 4:
			renpyable.delete_unused_DoA_files()
		elif answer == 5:
			renpyable.delete_old_ppf_files()
		elif answer == 6:
			renpyable.delete_old_pdf_to_ppf_files()
		elif answer == 7:
			renpyable.create_test_files(20)
		elif answer == 8:
			renpyable.delete_test_files()
			

import os
import shutil
import logging

logging.basicConfig(filename="Logs_generated.log", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO) 


def max_size(item):
	'''
	Given a list, it finds the second element of the list which is the size
	This is used for custom comparator in the sorting of List
	'''
	return int(item[1])


def get_actual_mapping_from_csv(filepath):
	'''
	Utility function to get the list of filename, filesize and location form the CSV file sorted on filesize in descending order which has information of the actual files
	filepath : r"C:\\Users\\sauravsaha\\Desktop\\test.csv"
	'''
	output = []
	filename = ""
	filesize = ""
	location = ""
	with open(filepath) as f:
		for line in f:
			line = line.split(',') 
			filename = line[0].strip()
			filesize = int(line[1].strip())
			location = line[2].strip()
			output.append([filename, filesize, location])	
	output.sort(key = max_size, reverse = True)
	return output


def get_recovered_file_mapping(recovery_directory):
	'''
	Utility method to get the list of filename and it's size sorted based on size in descending order from the directory where the Recovered Files of Recuva are stored.
	file_path=r"C:\\Users\\sauravsaha\\Desktop\\Testing"
	'''
	mapping=[]
	for _filename in os.listdir(recovery_directory):
		if os.path.isfile(recovery_directory+'\\'+ _filename):
			file_size = os.stat(recovery_directory+'\\'+ _filename).st_size
			mapping.append([_filename,file_size])
	mapping.sort(key = max_size, reverse = True)
	return mapping

def compare_filename(source_filename, target_filename):
	'''
	Utility method that compares the filename from the recovered directory to the filename mapping csv to check if the source file after normalization is same as that of the target filename.
	'''

	if '_' in source_filename:
		source_filename = source_filename[:source_filename.find('_')]+source_filename[source_filename.rfind('.'):]
	print(source_filename, target_filename)
	if target_filename == source_filename:
		return True
	return False


def moveAndRename(source_directory, source_filename, destination_directory, destination_filename):
	'''
	Utility Method to Move a File from One Directory to Another. In case, the directory doesn't already exist,
	directory is created and then the file is moved from source directory to the destination directory with
	the name of the file  as the destination filename
	conver to raw string
	'''
	if os.path.isdir(destination_directory) == False:
		os.makedirs(destination_directory)
	src_fullpath = source_directory + '\\' + source_filename
	dst_fullpath = destination_directory + '\\' + destination_filename
	shutil.move(src_fullpath, dst_fullpath)


def check_file_and_move(recovery_directory, actual_file_mapping,recovered_file_mapping):
	'''
	Core Logic of the Module which checks each file from the recovered file mapping to the actual file mapping and checks for size match and then filename match. If match is found, it is moved to the actual path after renaming and the entry from the actual file mapping is removed so that there are no duplicates.
	# recovery_directory = r"C:\\Users\\sauravsaha\\Desktop\\Testing"
	'''	
	
	for item_source in recovered_file_mapping:
		for item_target in actual_file_mapping:
			print(item_source, item_target)
			if item_source[1]==item_target[1]:
				#print(item_source[1], item_target[1])
				#print('Filesize Match')
				logger.info("[INFO] Recovered file size matches actual file size for the file %s", item_source[0])
				if compare_filename(item_source[0].strip(), item_target[0].strip()):
					
					logger.info("[INFO] Recovered filename %s matches actual filename %s", item_source[0], item_target[0]) 
					moveAndRename(recovery_directory, item_source[0].strip(),item_target[2], item_target[0].strip())
					actual_file_mapping.remove(item_target)
					logging.info('[INFO] Moving and renaming sucessful for %s', item_source[0])
					break
				else:
					logging.info('[INFO] Recovered file %s does not match with name of any', item_source[0])
			elif item_source[1] > item_target[1]:
				logging.warning('[WARNING] Recovered file %s does not match with size of any', item_source[0])
				break
			


if __name__ == "__main__":
	PATH_TO_CSV = r"C:\Users\sauravsaha\Desktop\test.csv"
	RECOVERY_DIRECTORY = r"C:\Users\sauravsaha\Desktop\Testing"
	actual_file_mapping = get_actual_mapping_from_csv(PATH_TO_CSV)
	recovered_file_mapping = get_recovered_file_mapping(RECOVERY_DIRECTORY)
	check_file_and_move(RECOVERY_DIRECTORY, actual_file_mapping, recovered_file_mapping)

'''
TODO:
1. Change the path of CSV and the Recovery Directory
2. Test the whole Program on a simulated environment for 1000 files
3. Remove all the debug statements of Print- DONE
4. Run the Program in Actual System on full files
'''
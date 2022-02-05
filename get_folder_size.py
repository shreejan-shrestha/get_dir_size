import os 

root_folder = 'd:\\pictures'

def get_folder_size(start = '.'):
    total_size = 0 
    for foldername, subfolder, filename in os.walk(root_folder):
        # print('The folders are ' + foldername)
        # print('The subfolders are ' + str(subfolder))
        # print('The files are ' + str(filename))
        for file in filename:
            filepath = os.path.join(foldername, file)
            # if not os.path.islink(filepath):
            total_size += os.path.getsize(filepath)
    
    return total_size

print(get_folder_size(root_folder), 'bytes')
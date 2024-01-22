import cryptography.fernet
import os

# This is to learn about how encryption works, not to create malware.

encryption_folder = os.path.expanduser("~/Documents/fernet_files")

def file_finder(directory):
    file_names = []
    folder = os.listdir(directory)
    if os.path.isfile(folder):
        file_names.append(folder)
    print(file_names)
    


file_finder(encryption_folder)

import cryptography.fernet
import os

# This is to learn about how encryption works, not to create malware.

encryption_folder = os.path.expanduser("~/Documents/fernet_files")

def file_finder(directory):
    file_names = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path):
            file_names.append(file)
    print(file_names)


file_finder(encryption_folder)

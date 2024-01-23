import os
from cryptography.fernet import Fernet


# WARNING READ THIS FILEPATH CAREFULLY!!!!!!
encryption_folder = os.path.expanduser("~/Documents/fernet_files")
# WARNING READ THIS FILEPATH CAREFULLY!!!!!!

def file_finder(directory):
    file_names = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path):
            file_names.append(full_path)
    print(file_names)
    return file_names

def encrypter(encryption):
    with open("crypt_key.key", "rb") as the_key:
        encryption_key = the_key.read()

    for file in encryption:
        with open(file, "rb") as read_file:
            contents = read_file.read()
        contents_encryped = Fernet(encryption_key).encrypt(contents)
        with open(file, "wb") as write_file:
            write_file.write(contents_encryped)

def decrypter(decryption):
    # same variables since theyre in different functions
    with open("crypt_key.key", "rb") as the_key:
        encryption_key = the_key.read()

    for file in decryption:
        with open(file, "rb") as read_file:
            contents = read_file.read()
        contents_decryped = Fernet(encryption_key).decrypt(contents)
        with open(file, "wb") as write_file:
            write_file.write(contents_decryped)


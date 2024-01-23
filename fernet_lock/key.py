from cryptography.fernet import Fernet

key_location = "~/Documents/git_hub/crypt_key.key"

crypt_key = Fernet.generate_key()

with open("crypt_key.key", "wb") as c_key:
    c_key.write(crypt_key)
